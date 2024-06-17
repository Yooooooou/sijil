from sqlalchemy import Integer, Column, ForeignKey, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped
from dependencies.database.db import Base


class DbRating(Base):
    __tablename__ = 'ratings'
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    rating: Mapped[float] = mapped_column(default=0)
    salon: Mapped["DbSalon"] = relationship("DbSalon", back_populates='rating', uselist=False)

    def __repr__(self):
        return f"{self.salon.name} {self.rating}"
