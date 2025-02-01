from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from utils import validate_admin

user_bp = APIRouter()

@user_bp.delete("/users/{user_id}", response_model=dict)
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(validate_admin)  
):
    """
    Elimina un usuario solo si el que lo solicita es un administrador.
    """
    # Verificar si el usuario autenticado tiene rol de administrador
    if current_user["role_id"] != 1:
        raise HTTPException(status_code=403, detail="Permission denied. Only administrators can perform this action.")

    # Buscar al usuario en la base de datos
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Eliminar el usuario
    db.delete(user)
    db.commit()

    return {"message": f"User with ID {user_id} successfully deleted"}
