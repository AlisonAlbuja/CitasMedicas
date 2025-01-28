from fastapi import APIRouter, HTTPException
from app.database.mysql import get_connection
from app.models.appointment import Appointment

router = APIRouter()

@router.post("/create")
async def create_appointment(appointment: Appointment):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO appointments (title, description, date, time)
        VALUES (%s, %s, %s, %s)
    """
    values = (appointment.title, appointment.description, appointment.date, appointment.time)
    cursor.execute(query, values)
    connection.commit()
    appointment.id = cursor.lastrowid
    cursor.close()
    connection.close()
    return {"id": appointment.id, "message": "Appointment created"}
