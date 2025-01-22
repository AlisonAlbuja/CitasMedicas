from pydantic import BaseModel, Field
from datetime import datetime

class Appointment(BaseModel):
    doctor_id: str = Field(..., description="ID del doctor")
    patient_id: str = Field(..., description="ID del paciente")
    date: datetime = Field(..., description="Fecha de la cita")
    description: str = Field(..., description="Descripción de la cita")
