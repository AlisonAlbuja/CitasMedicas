from fastapi import APIRouter, HTTPException
from app.database.mysql import get_connection

router = APIRouter()

@router.delete("/delete/{appointment_id}")
async def delete_appointment(appointment_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM appointments WHERE id = %s"
    cursor.execute(query, (appointment_id,))
    connection.commit()
    affected_rows = cursor.rowcount
    cursor.close()
    connection.close()
    if affected_rows == 0:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted"}
