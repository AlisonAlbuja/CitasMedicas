import jwt
from flask import request, jsonify
from jwt import ExpiredSignatureError, InvalidTokenError
import os

# JWT configurations from the login microservice's .env file
SECRET_KEY = "supersecretkey123"  # Make sure this matches the login microservice's key
ALGORITHM = "HS256"

def verify_admin(f):
    # Decorator to check if the user has an admin role
    def wrapper(*args, **kwargs):
        # Get the authorization header from the request
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'error': 'Authorization header missing'}), 401

        try:
            # Extract the token after "Bearer"
            token = auth_header.split(" ")[1]
        except IndexError:
            return jsonify({'error': 'Invalid token format'}), 401

        try:
            # Decode the JWT token
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            # Get the role_id field from the payload
            role_id = payload.get('role_id')
            if role_id != 1:  # Validate that role_id is 1 (admin)
                return jsonify({'error': 'Access restricted to administrators'}), 403
        except ExpiredSignatureError:
            return jsonify({'error': 'The token has expired'}), 401
        except InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401

        # If the token is valid, continue with the function execution
        return f(*args, **kwargs)
    
    return wrapper
