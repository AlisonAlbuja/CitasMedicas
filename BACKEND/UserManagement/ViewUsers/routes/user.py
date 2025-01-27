from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import User as UserSchema
from utils import verify_admin

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", response_model=list[UserSchema], dependencies=[Depends(verify_admin)])
async def get_all_users(db: Session = Depends(get_db)):
    """
    Endpoint para obtener todos los usuarios.
    Solo accesible por administradores.
    """
    users = db.query(User).all()
    return users
