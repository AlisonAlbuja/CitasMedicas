from fastapi import APIRouter, HTTPException, Depends, Request
from app.database.mysql import get_connection
from app.models.appointment import Appointment
from app.utils import verify_doctor  # ✅ Importar la validación de JWT

router = APIRouter()

@router.post("/create")
async def create_appointment(
    appointment: Appointment, 
    user: dict = Depends(verify_doctor)  # 🔥 Only Doctors can create appointments
):
    """ Create a new appointment if the authenticated user is a Doctor. """
    
    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    cursor = connection.cursor()
    try:
        query = """
            INSERT INTO appointments (title, description, date, time, doctor_name)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (appointment.title, appointment.description, appointment.date, appointment.time, user["sub"])  
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
