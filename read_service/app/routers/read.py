from fastapi import APIRouter, HTTPException
from app.database.mongodb import get_database
from bson import ObjectId

router = APIRouter()

@router.get("/appointments")
async def get_appointments():
    """Obtiene todas las citas guardadas en la base de datos."""
    db = get_database()
    appointments = list(db["appointments"].find())
    for appointment in appointments:
        appointment["_id"] = str(appointment["_id"])  # Convertir ObjectId a string
    return {"appointments": appointments}

@router.get("/appointments/{id}")
async def get_appointment_by_id(id: str):
    """Obtiene una cita específica por su ID."""
    try:
        # Convertir el ID en ObjectId
        object_id = ObjectId(id)

    except Exception:
        # Lanzar un error si el ID no es válido
        raise HTTPException(status_code=400, detail="Invalid ID format")

    db = get_database()
    appointment = db["appointments"].find_one({"_id": ObjectId(id)})
    
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    
    appointment["_id"] = str(appointment["_id"])  # Convertir ObjectId a string
    return {"appointment": appointment}
