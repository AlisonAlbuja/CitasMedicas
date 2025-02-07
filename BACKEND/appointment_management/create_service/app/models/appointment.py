from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Appointment(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=500)
    date: datetime
    time: str  # Puedes mejorar esto con un tipo `time`
    doctor_name: Optional[str] = Field(None, description="Name of the doctor who created the appointment")  # ✅ Cambiado

