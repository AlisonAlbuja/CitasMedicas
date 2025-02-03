from fastapi import APIRouter, HTTPException, Depends
from app.database.mysql import get_connection
from app.utils import verify_doctor  # ✅ Importar validación de JWT

router = APIRouter()

@router.delete("/appointments/{appointment_id}")
async def delete_appointment(appointment_id: int, user: dict = Depends(verify_doctor)):
    """
    Elimina una cita **solo si el doctor autenticado es el creador de la cita**.
    """
    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    cursor = connection.cursor()
    try:
        # 🔹 1. Verificar si la cita existe y pertenece al doctor autenticado
        check_query = "SELECT id FROM appointments WHERE id = %s AND doctor_name = %s"
        cursor.execute(check_query, (appointment_id, user["sub"]))
        appointment = cursor.fetchone()

        if not appointment:
            raise HTTPException(status_code=403, detail="No tienes permiso para eliminar esta cita o no existe.")

        # 🔹 2. Si el doctor es el creador, proceder con la eliminación
        delete_query = "DELETE FROM appointments WHERE id = %s AND doctor_name = %s"
        cursor.execute(delete_query, (appointment_id, user["sub"]))
        connection.commit()

        return {"message": "Cita eliminada correctamente ✅"}
    
    except Exception as err:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar la cita: {str(err)}")
    
    finally:
        cursor.close()
        connection.close()
