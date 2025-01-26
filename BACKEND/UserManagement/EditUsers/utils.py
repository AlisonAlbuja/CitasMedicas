import jwt
from flask import request, jsonify
from jwt import ExpiredSignatureError, InvalidTokenError
import os

# Configuraciones de JWT desde el archivo .env del microservicio de login
SECRET_KEY = "supersecretkey123"  # Reemplázalo si quieres cargarlo dinámicamente
ALGORITHM = "HS256"

def verify_admin(f):
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Authorization header missing'}), 401

        try:
            token = auth_header.split(" ")[1]
        except IndexError:
            return jsonify({'error': 'Invalid token format'}), 401

        try:
            # Decodificar el token JWT
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            role = payload.get('role')
            if role != 'admin':
                return jsonify({'error': 'Access restricted to administrators'}), 403
        except ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        except InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        return f(*args, **kwargs)
    return wrapper
