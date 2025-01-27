from fastapi import HTTPException, Request
import jwt
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

async def verify_admin(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Token no proporcionado")

    try:
        payload = jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("role_id") != 1:  # Validar si es administrador
            raise HTTPException(status_code=403, detail="Acceso denegado. Solo para administradores.")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
