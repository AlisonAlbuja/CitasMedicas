import requests
import os
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URL del servicio de login en AWS para validar tokens
LOGIN_SERVICE_URL = os.getenv("LOGIN_SERVICE_URL", "http://34.202.7.176:8000/auth/validate-token")

# Configuración de FastAPI para autenticación OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def verify_doctor(token: str = Depends(oauth2_scheme)):
    """
    Valida si el usuario autenticado tiene permisos de doctor consultando el servicio de login en AWS.
    """
    if not token:
        raise HTTPException(status_code=401, detail="Token requerido")

    try:
        # Hacer la petición al servicio de login para validar el token
        response = requests.get(LOGIN_SERVICE_URL, headers={"Authorization": f"Bearer {token}"})

        if response.status_code != 200:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")

        # Obtener los datos del usuario autenticado
        user_data = response.json()
        role_id = user_data.get("role_id")

        # Solo los doctores (role_id=2) pueden acceder
        if role_id != 2:
            raise HTTPException(status_code=403, detail="Acceso denegado. Solo doctores pueden acceder.")
        
        return user_data  # Retorna los datos del usuario autenticado

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Error al comunicarse con el servicio de autenticación")
