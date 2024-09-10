from pydantic import ConfigDict
from sqlalchemy import ForeignKey, Integer, String, UUID, DateTime, FLOAT
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class BaseTable(DeclarativeBase):

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        model_config = ConfigDict(from_attributes=True)


class PatientsTable(BaseTable):

    __tablename__ = "patients"

    patient_uuid: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, unique=True, server_default="uuid_generate_v4()")
    patient_name: Mapped[str] = mapped_column(String, nullable=True)
    patient_cpf: Mapped[str] = mapped_column(String, nullable=True)
    patient_gender: Mapped[str] = mapped_column(String, nullable=True)
    patient_birth_date: Mapped[str] = mapped_column(String, nullable=True)
    patient_birth_country: Mapped[str] = mapped_column(String, nullable=True)
    patient_phone: Mapped[str] = mapped_column(String, nullable=True)
    patient_observation: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default="now()")
    updated_at: Mapped[DateTime] = mapped_column(DateTime, nullable=True)
