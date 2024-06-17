from sqlalchemy import ForeignKey

from dependencies.database.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.service_model import DbService


class DbPrice(Base):
    __tablename__ = "prices"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    master_id: Mapped[int] = mapped_column(ForeignKey("masters.id"))
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"))
    price: Mapped[int] = mapped_column(nullable=False)

    # Связь Many-to-One с мастером и услугой
    master: Mapped["DbMaster"] = relationship("DbMaster", back_populates='services')
    service: Mapped["DbService"] = relationship("DbService", back_populates='prices')

    def __repr__(self):
        return f"{self.service.name} {self.master.first_name} {self.master.last_name} {self.price}"
