from fastapi import APIRouter, HTTPException
from app.database.mongodb import get_database
from pydantic import BaseModel
from bson.objectid import ObjectId  # Usa esto si necesitas ObjectId para MongoDB

router = APIRouter()

class UpdateAppointment(BaseModel):
    doctor_id: str | None = None
    patient_id: str | None = None
    date: str | None = None
    description: str | None = None

@router.put("/appointments/{id}")
async def update_appointment(id: str, appointment: UpdateAppointment):
    """Actualiza los datos de una cita existente."""
    db = get_database()
    update_data = {k: v for k, v in appointment.dict().items() if v is not None}

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided to update")

    result = db["appointments"].update_one({"_id": ObjectId(id)}, {"$set": update_data})

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return {"message": "Appointment updated successfully", "updated_fields": update_data}
