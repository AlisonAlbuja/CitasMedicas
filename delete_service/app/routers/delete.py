from fastapi import APIRouter, HTTPException
from app.database.mongodb import get_database
from bson.objectid import ObjectId

router = APIRouter()

@router.delete("/appointments/{id}")
async def delete_appointment(id: str):
    """Elimina una cita específica por su ID."""
    db = get_database()
    result = db["appointments"].delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return {"message": "Appointment deleted successfully"}
