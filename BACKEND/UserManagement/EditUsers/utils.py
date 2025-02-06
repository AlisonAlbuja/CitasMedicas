import os
import requests
from flask import request, jsonify
from functools import wraps
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

def verify_admin(f):
    """
    Decorador para verificar si el usuario tiene rol de administrador.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Obtener el encabezado Authorization
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Authorization header missing'}), 401

        try:
            # Extraer el token después de "Bearer"
            token = auth_header.split(" ")[1]
        except IndexError:
            return jsonify({'error': 'Invalid token format'}), 401

        try:
            # Enviar solicitud al microservicio de login para validar el token
            response = requests.get(LOGIN_SERVICE_URL, headers={"Authorization": f"Bearer {token}"})

            print(f"🔄 Enviando token para validación en {LOGIN_SERVICE_URL}...")

            if response.status_code != 200:
                print(f"⚠ Error en validación de token: {response.status_code} - {response.text}")
                return jsonify({'error': 'Invalid or expired token'}), 401

            # Decodificar la respuesta del login-service
            user_data = response.json()
            role_id = user_data.get("role_id")

            print(f"🔹 Respuesta del login-service: {user_data}")

            # Verificar si el usuario tiene rol de administrador (role_id=1)
            if role_id != 1:
                return jsonify({'error': 'Access restricted to administrators'}), 403

            # Si es válido, continuar con la ejecución de la función decorada
            return f(*args, **kwargs)

        except requests.exceptions.RequestException as e:
            print(f"❌ Error en la conexión con el login-service: {str(e)}")
            return jsonify({'error': 'Error connecting to authentication service'}), 500

    return wrapper

# Llamar a la función de prueba al iniciar el microservicio
test_login_service_connection()
