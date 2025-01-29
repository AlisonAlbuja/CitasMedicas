from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from database import get_db
from models import User
from utils import validate_admin

user_bp = APIRouter()

@user_bp.delete("/users/{user_id}", response_model=dict)
def delete_user(
    user_id: int, 
    username: str = Body(..., embed=True),  # Receive the username in the request body
    db: Session = Depends(get_db),
    is_admin: bool = Depends(validate_admin)
):
    # Search for the user by ID and name
    user = db.query(User).filter(User.id == user_id, User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found or incorrect data")
    
    # Delete the user
    db.delete(user)
    db.commit()
    return {"message": f"User with ID {user_id} and name {username} successfully deleted"}
