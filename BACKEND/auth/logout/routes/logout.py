from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
import redis
import os

router = APIRouter()
security = HTTPBearer()

# Conectar con Redis compartido
redis_host = os.getenv("REDIS_HOST", "redis-shared")  # 🔹 Asegurar que usa Redis compartido
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@router.post("/logout")
def logout(token: str = Depends(security)):
    """Cierra la sesión invalidando el token en Redis"""

    token_key = f"blacklist:{token.credentials}"  # 🔹 Prefijo para la lista negra

    # Verificar si el token ya está en la lista negra
    if redis_client.exists(token_key):
        raise HTTPException(status_code=400, detail="Token ya ha sido invalidado")

    # Agregar token a la lista negra y establecer tiempo de expiración
    redis_client.set(token_key, "invalid", ex=3600)  # 🔹 Expira en 1 hora

    return {"message": "Sesión cerrada exitosamente"}
