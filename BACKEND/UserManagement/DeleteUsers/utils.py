from dotenv import load_dotenv
import os
import requests
from fastapi import HTTPException, Header

# Cargar variables de entorno
load_dotenv()

# 🔧 Eliminar cualquier dirección IP y asegurarnos de usar localhost (para pruebas locales)
LOGIN_SERVICE_URL = os.getenv("LOGIN_SERVICE_URL", "http://localhost:8000")

def validate_admin(Authorization: str = Header(None)):
    """Valida el token con el microservicio de login y verifica si el usuario es administrador"""
    if not Authorization:
        raise HTTPException(status_code=401, detail="Token required")

    try:
        token = Authorization.split(" ")[1]  # Extraer el token del encabezado

        # 📌 Validar el token con el microservicio de login
        response = requests.get(f"{LOGIN_SERVICE_URL}/validate-token", headers={"Authorization": f"Bearer {token}"})

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Invalid or expired token")

        user_data = response.json()
        
        # 📌 Verificar que el usuario tenga rol de administrador
        role_id = user_data.get("role_id")
        if role_id != 1:  
            raise HTTPException(status_code=403, detail="Permission denied. Only administrators can perform this action.")
        
        return user_data  # Retornar los datos del usuario autenticado
    
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication failed: {str(e)}")
