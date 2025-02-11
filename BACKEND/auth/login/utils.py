from dotenv import load_dotenv
import os
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
import redis
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer

# load environment variables
load_dotenv()

# Connect to Redis for token invalidation
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

# Configuración de seguridad
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "fallbacksecretkey")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

oauth2_scheme = HTTPBearer()

# Funciones para manejo de contraseñas
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Función para crear un JWT token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Función para decodificar un JWT token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

# ✅ Nueva función para verificar si un token es válido o ha sido invalidado en Redis
def verify_token(token: str = Depends(oauth2_scheme)):
    """Verifica si el token es válido y no ha sido invalidado en Redis"""
    try:
        # Revisar si el token está en la lista negra de Redis
        if redis_client.get(token.credentials):
            raise HTTPException(status_code=401, detail="Token inválido")

        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]  # Retorna el ID del usuario autenticado
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
