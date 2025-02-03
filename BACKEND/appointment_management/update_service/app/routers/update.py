from fastapi import APIRouter, HTTPException, Depends, Request
from app.database.mysql import get_connection
from app.models.appointment import Appointment
from app.utils import verify_doctor  # ✅ Importamos la validación de JWT

router = APIRouter()

@router.put("/appointments/{appointment_id}")
async def update_appointment(
    appointment_id: int, 
    appointment: Appointment, 
    user: dict = Depends(verify_doctor)  # 🔥 Solo Doctores pueden actualizar citas
):
    """ Actualiza una cita si el usuario autenticado es un Doctor. """

    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    cursor = connection.cursor()
    try:
        # Verificar que la cita existe antes de actualizar
        cursor.execute("SELECT id FROM appointments WHERE id = %s", (appointment_id,))
        existing_appointment = cursor.fetchone()

        if not existing_appointment:
            raise HTTPException(status_code=404, detail="Cita no encontrada")

        query = """
            UPDATE appointments 
            SET title = %s, description = %s, date = %s, time = %s, updated_at = NOW()
            WHERE id = %s
        """
        values = (appointment.title, appointment.description, appointment.date, appointment.time, appointment_id)
        cursor.execute(query, values)
        connection.commit()

        return {"message": "Cita actualizada correctamente ✅"}
    except Exception as err:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error en la BD: {str(err)}")
    finally:
        cursor.close()
        connection.close()
