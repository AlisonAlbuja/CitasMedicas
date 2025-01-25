from dotenv import load_dotenv
import os
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta

# Cargar las variables de entorno
load_dotenv()

# Contexto de cifrado para contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Clave secreta y algoritmo para JWT
SECRET_KEY = os.getenv("SECRET_KEY", "fallbacksecretkey")  # Cargar clave desde entorno
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Funciones para gestión de contraseñas
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Función para crear un token JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Función para decodificar un token JWT
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
