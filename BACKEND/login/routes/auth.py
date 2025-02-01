from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import UserCreate, UserLogin
from models import User
from database import SessionLocal
from utils import get_password_hash, verify_password, create_access_token, decode_access_token
from fastapi.security import OAuth2PasswordBearer
import redis
import os

router = APIRouter()

# 📌 Configuración de Redis
redis_host = os.getenv("REDIS_HOST", "redis")  
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# 📌 Esquema de autenticación OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login") 

# 📌 Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📌 Registro de usuario (Solo Pacientes)
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    patient_role_id = 3  # 🔧 Corrección del ID de pacientes
    hashed_password = get_password_hash(user.password)
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role_id=patient_role_id
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully as patient"} 

# 📌 Login con generación de token JWT
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    user_in_db = db.query(User).filter(User.username == user.username).first()
    
    if not user_in_db or not verify_password(user.password, user_in_db.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # 📌 Generar Token JWT con información del usuario
    token = create_access_token({
        "sub": user_in_db.username,  
        "role_id": user_in_db.role_id  
    })

    return {"access_token": token, "token_type": "bearer"}

# 📌 Nueva función para validar token y extraer datos del usuario
@router.get("/validate-token")
def validate_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Valida el token y devuelve la información del usuario autenticado"""
    try:
        # 📌 Revisar si el token está en la lista negra de Redis
        if redis_client.get(token):
            raise HTTPException(status_code=401, detail="Token inválido o expirado")

        # 📌 Decodificar el token
        payload = decode_access_token(token)
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")

        username = payload.get("sub")
        user = db.query(User).filter(User.username == username).first()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "username": user.username,
            "role_id": user.role_id
        }

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
