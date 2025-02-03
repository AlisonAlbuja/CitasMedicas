import jwt
from fastapi import Request, HTTPException, Depends
from jwt import ExpiredSignatureError, InvalidTokenError
import os

# 🔹 Configuración del JWT, asegúrate de que coincida con `login-service`
SECRET_KEY = "supersecretkey123"  # Usa el mismo SECRET_KEY que `login-service`
ALGORITHM = "HS256"

def verify_doctor(request: Request):
    """ Verifica si el usuario autenticado es un Doctor (role_id == 2). """
    auth_header = request.headers.get('Authorization')
    
    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    try:
        # Extraer token del formato "Bearer <token>"
        token = auth_header.split(" ")[1]
    except IndexError:
        raise HTTPException(status_code=401, detail="Invalid token format")

    try:
        # Decodificar el token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role_id = payload.get('role_id')
        
        # 🔹 Solo permite acceso a los doctores
        if role_id != 2:
            raise HTTPException(status_code=403, detail="Access restricted to doctors")

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return payload  # Devuelve la información del usuario autenticado
