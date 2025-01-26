from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from database import get_db
from models import User
from utils import validate_admin

user_bp = APIRouter()

@user_bp.delete("/users/{user_id}", response_model=dict)
def delete_user(
    user_id: int, 
    username: str = Body(..., embed=True),  # Recibe el nombre del usuario en el cuerpo de la solicitud
    db: Session = Depends(get_db),
    is_admin: bool = Depends(validate_admin)
):
    # Buscar al usuario por ID y nombre
    user = db.query(User).filter(User.id == user_id, User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado o datos incorrectos")
    
    # Eliminar al usuario
    db.delete(user)
    db.commit()
    return {"message": f"Usuario con ID {user_id} y nombre {username} eliminado exitosamente"}
