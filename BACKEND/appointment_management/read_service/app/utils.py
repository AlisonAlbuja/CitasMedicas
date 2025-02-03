import jwt
from fastapi import Request, HTTPException, Depends
from jwt import ExpiredSignatureError, InvalidTokenError

# 🔹 Configuración del JWT (debe coincidir con el servicio de login)
SECRET_KEY = "supersecretkey123"  # Debe ser la misma clave que usa `login-service`
ALGORITHM = "HS256"

def verify_user(request: Request):
    """ Verifica el JWT del usuario sin depender de `login-service` """
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    try:
        # Extraer el token del formato "Bearer <token>"
        token = auth_header.split(" ")[1]
    except IndexError:
        raise HTTPException(status_code=401, detail="Invalid token format")

    try:
        # 🔥 Decodificar el token localmente sin llamar a `login-service`
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Devuelve los datos del usuario autenticado

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
