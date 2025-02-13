from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
import redis
import os

router = APIRouter()
security = HTTPBearer()

# Connect with shared Redis
redis_host = os.getenv("REDIS_HOST", "redis-shared")  # 🔹 Ensure you use shared Redis
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@router.post("/logout")
def logout(token: str = Depends(security)):
    """Cierra la sesión invalidando el token en Redis"""

    token_key = f"blacklist:{token.credentials}"  # 🔹 Prefijo para la lista negra

    # Check if the token is already
    if redis_client.exists(token_key):
        raise HTTPException(status_code=400, detail="Token ya ha sido invalidado")

    # Add token to the blacklist and set expiration time
    redis_client.set(token_key, "invalid", ex=3600)  # 🔹 Expira en 1 hora

    return {"message": "Sesión cerrada exitosamente"}
