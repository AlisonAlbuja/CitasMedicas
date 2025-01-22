from fastapi import APIRouter, HTTPException
from app.models.appointment import Appointment
from app.database.mongodb import get_database

router = APIRouter()

@router.post("/appointments")
async def create_appointment(appointment: Appointment):
    """Crea una nueva cita en la base de datos."""
    db = get_database()
    result = db["appointments"].insert_one(appointment.dict())
    if not result.acknowledged:
        raise HTTPException(status_code=500, detail="Failed to create appointment")
    return {
        "message": "Appointment created successfully",
        "appointment_id": str(result.inserted_id)
    }