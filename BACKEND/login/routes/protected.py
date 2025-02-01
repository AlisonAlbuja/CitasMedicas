from fastapi import APIRouter, Depends, HTTPException
from utils import verify_token
import redis
import os

router = APIRouter()

# Conectar con Redis compartido
redis_host = os.getenv("REDIS_HOST", "redis-shared")  # Asegurarse de usar Redis compartido
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def verificar_token_en_redis(token: str = Depends(verify_token)):
    """Verifica si el token está en la lista negra de Redis antes de permitir el acceso."""
    if redis_client.exists(f"blacklist:{token}"):
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return token

@router.get("/dashboard")
def dashboard(user_id: str = Depends(verificar_token_en_redis)):
    return {"message": f"Bienvenido usuario {user_id}"}
