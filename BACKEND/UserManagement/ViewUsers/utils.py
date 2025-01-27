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
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token no proporcionado o mal formado")

    try:
        token = token.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Verificar si el rol es de administrador
        if payload.get("role_id") != 1:  # role_id debe ser 1 para administrador
            raise HTTPException(status_code=403, detail="Acceso denegado. Solo para administradores.")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
