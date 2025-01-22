from pymongo import MongoClient
import os

def get_database():
    """Devuelve la conexión a la base de datos MongoDB."""
    mongo_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    client = MongoClient(mongo_uri)
    return client["appointments_db"]  # Base de datos correcta
