from fastapi import APIRouter, HTTPException
from app.database.mysql import get_connection
from app.models.appointment import Appointment

router = APIRouter()

@router.post("/create")
async def create_appointment(appointment: Appointment):
    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")
    
    cursor = connection.cursor()
    try:
        query = """
            INSERT INTO appointments (title, description, date, time)
            VALUES (%s, %s, %s, %s)
        """
        values = (appointment.title, appointment.description, appointment.date, appointment.time)
        cursor.execute(query, values)
        connection.commit()

        appointment.id = cursor.lastrowid
        return {"id": appointment.id, "message": "Cita creada correctamente ✅"}
    except Exception as err:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error en la BD: {str(err)}")
    finally:
        cursor.close()
        connection.close()
