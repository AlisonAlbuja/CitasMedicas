from fastapi import HTTPException, Request
import jwt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

async def verify_admin(request: Request):
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token not provided or malformed")

    try:
        token = token.split(" ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Verify if the role is admin
        if payload.get("role_id") != 1:  # role_id should be 1 for admin
            raise HTTPException(status_code=403, detail="Access denied. Admins only.")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
