from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from dependencies.database.db import Base


# from models.review_model import DbReview  # Assuming DbReview model exists


class DbUser(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(default=None)

    # Relationship to DbReview
    reviews: Mapped[list["DbReview"]] = relationship("DbReview", back_populates='user')
    appointments: Mapped[list["DbAppointment"]] = relationship("DbAppointment", back_populates="user")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    from models.appointment_model import DbAppointment
