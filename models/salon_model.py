from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from dependencies.database.db import Base
from models.salon_rating_model import DbRating  # Import the related class here


class DbSalon(Base):
    __tablename__ = "salons"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    address: Mapped[str] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    rating_id: Mapped[int | None] = mapped_column(ForeignKey('ratings.id'), nullable=True)
    review_count: Mapped[int] = mapped_column(default=0)

    # One-to-one relationship to DbRating
    rating: Mapped["DbRating"] = relationship("DbRating", back_populates='salon', uselist=False)
    reviews: Mapped[list["DbReview"]] = relationship("DbReview", back_populates='salon')

    def __repr__(self):
        return f"{self.name}"
