from fastapi import APIRouter, HTTPException, Depends, Request
from app.database.mysql import get_connection
from app.models.appointment import Appointment
from app.utils import verify_doctor  # ✅ We import the JWT validation

router = APIRouter()

@router.put("/appointments/{appointment_id}")
async def update_appointment(
    appointment_id: int, 
    appointment: Appointment, 
    user: dict = Depends(verify_doctor)  # 🔥 Only Doctors can update appointments
):
    """ Update an appointment if the authenticated user is a Doctor. """

    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error connecting to database")

    cursor = connection.cursor()
    try:
        # Verify that the appointment exists before updating
        cursor.execute("SELECT id FROM appointments WHERE id = %s", (appointment_id,))
        existing_appointment = cursor.fetchone()

        if not existing_appointment:
            raise HTTPException(status_code=404, detail="Quote not found")

        query = """
            UPDATE appointments 
            SET title = %s, description = %s, date = %s, time = %s, updated_at = NOW()
            WHERE id = %s
        """
        values = (appointment.title, appointment.description, appointment.date, appointment.time, appointment_id)
        cursor.execute(query, values)
        connection.commit()

        return {"message": "Citation updated successfully ✅"}
    except Exception as err:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error in BD: {str(err)}")
    finally:
        cursor.close()
        connection.close()
