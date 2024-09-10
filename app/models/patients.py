from typing import Optional
from pydantic import BaseModel, Field
from sqlalchemy import ForeignKey, Integer, String, UUID, DateTime, FLOAT

class Patient(BaseModel):
    patient_uuid: UUID
    patient_name: str