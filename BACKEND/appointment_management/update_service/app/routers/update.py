from fastapi import APIRouter, HTTPException
from app.database.mysql import get_connection
from app.models.appointment import Appointment

router = APIRouter()

@router.put("/update/{appointment_id}")
async def update_appointment(appointment_id: int, appointment: Appointment):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        UPDATE appointments
        SET title = %s, description = %s, date = %s, time = %s
        WHERE id = %s
    """
    values = (appointment.title, appointment.description, appointment.date, appointment.time, appointment_id)
    cursor.execute(query, values)
    connection.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    connection.close()
    if affected_rows == 0:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment updated"}
