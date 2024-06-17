from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from dependencies.database.db import Base
from models.user_model import DbUser
from models.salon_model import DbSalon
from models.master_model import DbMaster


class DbReview(Base):
    __tablename__ = 'reviews'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    salon_id: Mapped[int] = mapped_column(ForeignKey('salons.id'))
    master_id: Mapped[int] = mapped_column(ForeignKey('masters.id'), nullable=True)
    score: Mapped[int] = mapped_column()
    comment: Mapped[str] = mapped_column(nullable=True)

    salon: Mapped["DbSalon"] = relationship("DbSalon", back_populates='reviews')
    user: Mapped["DbUser"] = relationship("DbUser", back_populates='reviews')
    master: Mapped["DbMaster"] = relationship("DbMaster", back_populates='reviews')

    def __repr__(self):
        return f"{self.user.first_name} {self.user.last_name} set score = {self.score} to salon {self.salon.name}"
