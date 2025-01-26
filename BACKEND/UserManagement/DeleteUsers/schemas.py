from pydantic import BaseModel
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role_id: int
    created_at: datetime

    class Config:
        orm_mode = True
