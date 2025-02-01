import jwt
import os
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer
from database import redis_client
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = HTTPBearer()

def verify_token(token: str = Depends(oauth2_scheme)):
    """Verifica si un token es válido y no está en Redis."""
    try:
        # Revisar si el token está en Redis (lista negra)
        if redis_client.get(token.credentials):
            raise HTTPException(status_code=401, detail="Token inválido")

        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]  # Retorna el ID del usuario autenticado
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")

def invalidate_token(token: str):
    """Añade el token a Redis con expiración (blacklist)."""
    redis_client.setex(token, 3600, "invalidated")  # Expira en 1 hora
