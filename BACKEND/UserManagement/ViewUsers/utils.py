from fastapi import HTTPException, Request
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URL del servicio de login en AWS para validar tokens
LOGIN_SERVICE_URL = os.getenv("LOGIN_SERVICE_URL", "http://34.202.7.176:8000/auth/validate-token")

def test_login_service_connection():
    """
    Prueba la conexión con el microservicio de Login en AWS.
    """
    try:
        response = requests.get(LOGIN_SERVICE_URL)
        if response.status_code == 200:
            print(f"✅ Conexión exitosa con {LOGIN_SERVICE_URL}")
        else:
            print(f"⚠ Error en conexión: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"❌ No se pudo conectar al servicio de Login: {str(e)}")

async def verify_admin(request: Request):
    """
    Valida si el usuario autenticado tiene rol de administrador llamando al servicio de login en AWS.
    """
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token no proporcionado o mal formado")

    try:
        # Extraer el token después de "Bearer "
        token = token.split(" ")[1]

        # Hacer la petición al servicio de login para validar el token
        response = requests.get(LOGIN_SERVICE_URL, headers={"Authorization": f"Bearer {token}"})

        print(f"🔄 Enviando token para validación en {LOGIN_SERVICE_URL}...")

        if response.status_code != 200:
            print(f"⚠ Error en validación de token: {response.status_code} - {response.text}")
            raise HTTPException(status_code=401, detail="Token inválido o expirado")

        # Obtener los datos del usuario autenticado
        user_data = response.json()
        role_id = user_data.get("role_id")

        print(f"🔹 Respuesta del login-service: {user_data}")

        # Solo los administradores (role_id=1) pueden acceder
        if role_id != 1:
            raise HTTPException(status_code=403, detail="Acceso denegado. Solo administradores pueden acceder.")
        
        return user_data  # Retorna los datos del usuario autenticado

    except requests.exceptions.RequestException as e:
        print(f"❌ Error en la conexión con el login-service: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al comunicarse con el servicio de autenticación")

# Llamar a la función de prueba al iniciar el microservicio
test_login_service_connection()
