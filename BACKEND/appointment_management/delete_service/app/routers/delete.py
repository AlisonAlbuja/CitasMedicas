from fastapi import APIRouter, HTTPException, Depends
from app.database.mysql import get_connection
from app.utils import verify_doctor  # ✅ Import JWT validation

router = APIRouter()

@router.delete("/appointments/{appointment_id}")
async def delete_appointment(appointment_id: int, user: dict = Depends(verify_doctor)):
    """
    Delete an appointment **only if the authenticated doctor is the creator of the appointment**.    """
    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error connecting to database")

    cursor = connection.cursor()
    try:
        # 🔹 1. Check if the appointment exists and belongs to the authenticated doctor
        check_query = "SELECT id FROM appointments WHERE id = %s AND doctor_name = %s"
        cursor.execute(check_query, (appointment_id, user["sub"]))
        appointment = cursor.fetchone()

        if not appointment:
            raise HTTPException(status_code=403, detail="You do not have permission to delete this quote or it does not exist.")

        # 🔹 2. If the doctor is the creator, proceed with the removal
        delete_query = "DELETE FROM appointments WHERE id = %s AND doctor_name = %s"
        cursor.execute(delete_query, (appointment_id, user["sub"]))
        connection.commit()

        return {"message": "Quote successfully deleted ✅"}
    
    except Exception as err:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting appointment: {str(err)}")
    
    finally:
        cursor.close()
        connection.close()
