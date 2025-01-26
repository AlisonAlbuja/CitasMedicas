from dotenv import load_dotenv
import os
from jose import jwt, JWTError
from fastapi import HTTPException, Header

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "fallbacksecretkey")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

def validate_admin(Authorization: str = Header(None)):
    if not Authorization:
        raise HTTPException(status_code=401, detail="Token requerido")
    
    try:
        token = Authorization.split(" ")[1]
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        role_id = decoded.get("role_id")
        if role_id != 1:  
            raise HTTPException(status_code=403, detail="Permiso denegado. Solo administradores pueden realizar esta acción.")
        return decoded  
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
