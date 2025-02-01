from fastapi import APIRouter, HTTPException
from app.database.mysql import get_connection

router = APIRouter()

@router.delete("/appointments/{appointment_id}")
async def delete_appointment(appointment_id: int):
    """
    Elimina una cita de la base de datos.
    """
    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    cursor = connection.cursor()
    try:
        query = "DELETE FROM appointments WHERE id = %s"
        cursor.execute(query, (appointment_id,))
        connection.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Cita no encontrada")

        return {"message": "Cita eliminada correctamente ✅"}
    except Exception as err:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar la cita: {str(err)}")
    finally:
        cursor.close()
        connection.close()
