from pydantic import BaseModel
from typing import Optional

class Appointment(BaseModel):
    id: Optional[int]
    title: str
    description: str
    date: str
    time: str
