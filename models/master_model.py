from sqlalchemy import ForeignKey
from dependencies.database.db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.master_rating_model import DbMasterRating
from models.service_price_model import DbPrice


class DbMaster(Base):
    __tablename__ = "masters"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    experience: Mapped[int] = mapped_column(default=0)
    rating_id: Mapped[int | None] = mapped_column(ForeignKey('master_ratings.id'), nullable=True)
    available: Mapped[bool] = mapped_column(default=True)
    bio: Mapped[str] = mapped_column(nullable=True)

    # One-to-One relationship with DbMasterRating
    rating: Mapped["DbMasterRating"] = relationship("DbMasterRating", back_populates="master", uselist=False)

    # One-to-Many relationship with DbPrice and DbAppointment
    services: Mapped[list["DbPrice"]] = relationship("DbPrice", back_populates='master')
    appointments: Mapped[list["DbAppointment"]] = relationship("DbAppointment", back_populates="master")
    reviews: Mapped[list["DbReview"]] = relationship("DbReview", back_populates="master")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
