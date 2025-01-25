from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import UserCreate, Token
from models import User
from database import SessionLocal
from utils import get_password_hash, verify_password, create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    admin_role_id = 3
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role_id=admin_role_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully as administrator"}

from schemas import UserLogin

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    user_in_db = db.query(User).filter(User.username == user.username).first()
    if not user_in_db or not verify_password(user.password, user_in_db.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

  
    token = create_access_token({
        "sub": user_in_db.username,  
        "role_id": user_in_db.role_id  
    })

    return {"access_token": token, "token_type": "bearer"}


@router.get("/test")
def test_endpoint():
    return {"message": "Test successful"}
