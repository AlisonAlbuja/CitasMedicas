import redis
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Connect with Redis
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis-logout"),  # 🔹 Cambiado de "localhost" a "redis-logout"
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)
