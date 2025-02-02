from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base de datos principal (Login/Admin)
DATABASE_URL = config("DATABASE_URL")

# Base de datos de doctores
DOCTOR_DATABASE_URL = config("DOCTOR_DATABASE_URL")

# Diccionario para manejar múltiples bases de datos
DATABASES = {
    "1": DATABASE_URL,         # Admins
    "2": DOCTOR_DATABASE_URL,  # Doctores
}

# Crear motores y sesiones de base de datos
engines = {role_id: create_engine(url) for role_id, url in DATABASES.items()}
SessionLocals = {role_id: sessionmaker(autocommit=False, autoflush=False, bind=engine)
                 for role_id, engine in engines.items()}

Base = declarative_base()

# ✅ Nueva función corregida para obtener la sesión de base de datos
def get_db(role_id: str):
    """Devuelve directamente una sesión de base de datos según el rol del usuario."""
    if role_id not in SessionLocals:
        raise ValueError(f"Rol no reconocido: {role_id}, no se puede conectar a la base de datos")

    db = SessionLocals[role_id]()
    return db
