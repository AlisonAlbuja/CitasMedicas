from fastapi import APIRouter, HTTPException
from app.database.mysql import get_connection
from app.models.appointment import Appointment  # Asegurar que esta línea está presente

router = APIRouter()

@router.put("/appointments/{appointment_id}")
async def update_appointment(appointment_id: int, appointment: Appointment):
    """
    Actualiza una cita existente en la base de datos.
    """
    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    cursor = connection.cursor()
    try:
        query = """
            UPDATE appointments
            SET title = %s, description = %s, date = %s, time = %s
            WHERE id = %s
        """
        values = (appointment.title, appointment.description, appointment.date, appointment.time, appointment_id)
        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cita no encontrada")

        return {"message": "Cita actualizada correctamente ✅"}
    except Exception as err:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error al actualizar la cita: {str(err)}")
    finally:
        cursor.close()
        connection.close()
