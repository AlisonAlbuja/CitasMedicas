from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils import verify_token
from database import get_db
import redis
import os

router = APIRouter()

# Conectar con Redis compartido
redis_host = os.getenv("REDIS_HOST", "redis-shared")  # Asegurarse de usar Redis compartido
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def verificar_token_en_redis(token_data: dict = Depends(verify_token)):
    """Verifica si el token está en la lista negra de Redis antes de permitir el acceso."""
    if redis_client.exists(f"blacklist:{token_data['sub']}"):
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    return token_data

@router.get("/dashboard")
def dashboard(
    token_data: dict = Depends(verificar_token_en_redis),
    db: Session = Depends(lambda: next(get_db(token_data["role_id"])) if token_data["role_id"] in ["1", "2"] else None)
):
    """Determina el tipo de usuario y lo redirige al dashboard adecuado."""
    
    role_id = token_data.get("role_id")
    user_id = token_data.get("sub")

    if role_id == "1":
        return {"message": f"Bienvenido ADMIN {user_id}, acceso a panel de administración."}
    elif role_id == "2":
        return {"message": f"Bienvenido DOCTOR {user_id}, acceso a citas y gestión médica."}
    elif role_id == "3":
        return {"message": f"Bienvenido PACIENTE {user_id}, acceso a su dashboard. (Sin base de datos aún)."}
    else:
        raise HTTPException(status_code=403, detail="Acceso denegado. Rol no autorizado.")
