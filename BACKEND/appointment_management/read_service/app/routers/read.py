from fastapi import APIRouter, HTTPException, Depends
from app.database.mysql import get_connection
from app.utils import verify_user 

router = APIRouter()

@router.get("/appointments", tags=["appointments"])
async def get_appointments(user: dict = Depends(verify_user)):  
    """
    Obtains all citations stored in the database, authenticating the user.
    """
    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, title, description, date, time FROM appointments")
        appointments = cursor.fetchall()
        
        results = [
            {"id": row["id"], "title": row["title"], "description": row["description"], "date": row["date"], "time": row["time"]}
            for row in appointments
        ]
        
        return {"appointments": results}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener citas: {str(err)}")
    finally:
        cursor.close()
        connection.close()


@router.get("/appointments/{appointment_id}", tags=["appointments"])
async def get_appointment_by_id(appointment_id: int, user: dict = Depends(verify_user)):  
    """
    Obtiene una cita específica por su ID, autenticando al usuario.
    """
    connection = get_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="Error en la conexión a la base de datos")

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, title, description, date, time FROM appointments WHERE id = %s", (appointment_id,))
        appointment = cursor.fetchone()

        if not appointment:
            raise HTTPException(status_code=404, detail=f"Cita con ID {appointment_id} no encontrada")

        return {
            "id": appointment["id"],
            "title": appointment["title"],
            "description": appointment["description"],
            "date": appointment["date"],
            "time": appointment["time"]
        }
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener la cita: {str(err)}")
    finally:
        cursor.close()
        connection.close()
