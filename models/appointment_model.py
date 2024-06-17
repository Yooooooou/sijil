from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from dependencies.database.db import Base
from datetime import datetime
from models.master_model import DbMaster


class DbAppointment(Base):
    __tablename__ = "appointments"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    appointment_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    master_id: Mapped[int] = mapped_column(ForeignKey("masters.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    appointment_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Many-to-One relationship with user, master, and service
    user: Mapped["DbUser"] = relationship("DbUser", back_populates="appointments", lazy='select')
    master: Mapped["DbMaster"] = relationship("DbMaster", back_populates="appointments", lazy="select")
    service: Mapped["DbService"] = relationship("DbService")

    def __repr__(self):
        return f"Appointment at {self.appointment_date} with master_id {self.master_id} for service_id {self.service_id}"
