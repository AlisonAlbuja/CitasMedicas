import os
import requests
from fastapi import HTTPException, Header
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# URL del servicio de login en AWS
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

def verify_doctor(Authorization: str = Header(None)):
    """
    Valida si el usuario autenticado tiene rol de Doctor consultando el servicio de Login en AWS.
    """
    if not Authorization:
        raise HTTPException(status_code=401, detail="Token requerido")

    try:
        token = Authorization.split(" ")[1]

        # 📌 Hacer petición HTTP al servicio de Login para validar el token
        response = requests.get(LOGIN_SERVICE_URL, headers={"Authorization": f"Bearer {token}"})

        print(f"🔄 Enviando token para validación en {LOGIN_SERVICE_URL}...")

        if response.status_code != 200:
            print(f"⚠ Error en validación de token: {response.status_code} - {response.text}")
            raise HTTPException(status_code=401, detail="Token inválido o expirado")

        # 📌 Decodificar respuesta del login-service
        user_data = response.json()
        role_id = user_data.get("role_id")

        print(f"🔹 Respuesta del login-service: {user_data}")

        # 📌 Solo los doctores (role_id=2) pueden continuar
        if role_id != 2:
            raise HTTPException(status_code=403, detail="Acceso restringido solo para doctores.")

        return user_data  # Devuelve los datos del usuario autenticado

    except requests.exceptions.RequestException as e:
        print(f"❌ Error en la conexión con el login-service: {str(e)}")
        raise HTTPException(status_code=500, detail="Error al comunicarse con el servicio de autenticación")

# Llamar a la función de prueba al iniciar el microservicio
test_login_service_connection()
