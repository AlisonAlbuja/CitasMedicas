from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import UserCreate, UserLogin, Token
from models import User
from database import SessionLocal
from utils import get_password_hash, verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer
import redis
import os

router = APIRouter()

# Configuración de Redis
redis_host = os.getenv("REDIS_HOST", "redis-shared")  # Asegúrate de usar el Redis compartido
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Esquema de autenticación
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    admin_role_id = 3
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role_id=admin_role_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully as administrator"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    user_in_db = db.query(User).filter(User.username == user.username).first()
    if not user_in_db or not verify_password(user.password, user_in_db.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({
        "sub": user_in_db.username,  
        "role_id": user_in_db.role_id  
    })

    return {"access_token": token, "token_type": "bearer"}

def verificar_token(token: str = Depends(oauth2_scheme)):
    """Verifica si el token está en la lista negra de Redis"""
    if redis_client.exists(f"blacklist:{token}"):
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return token  # Devuelve el token si es válido

@router.get("/test-auth")
def test_auth(token: str = Depends(verificar_token)):
    """Ruta de prueba para verificar la autenticación"""
    return {"message": "Autenticación exitosa", "token": token}
