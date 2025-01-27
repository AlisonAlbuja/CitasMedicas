import jwt
from flask import request, jsonify
from jwt import ExpiredSignatureError, InvalidTokenError
import os

# Configuraciones de JWT desde el archivo .env del microservicio de login
SECRET_KEY = "supersecretkey123"  # Asegúrate de que sea consistente con el microservicio de login
ALGORITHM = "HS256"

def verify_admin(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Authorization header missing'}), 401

        try:
            token = auth_header.split(" ")[1]  # Extraer el token después de "Bearer"
        except IndexError:
            return jsonify({'error': 'Invalid token format'}), 401

        try:
            # Decodificar el token JWT
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            role_id = payload.get('role_id')  # Obtener el campo role_id
            if role_id != 1:  # Validar que role_id sea 1 (admin)
                return jsonify({'error': 'Access restricted to administrators'}), 403
        except ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return f(*args, **kwargs)
    return wrapper
