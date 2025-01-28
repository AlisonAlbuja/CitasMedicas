from fastapi import APIRouter, HTTPException
from app.database.mysql import get_connection

router = APIRouter()

@router.get("/read/{appointment_id}")
async def read_appointment(appointment_id: int):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM appointments WHERE id = %s"
    cursor.execute(query, (appointment_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if not result:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return result
