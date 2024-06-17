from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dependencies.database.db import Base


class DbMasterRating(Base):
    __tablename__ = "master_ratings"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    rating: Mapped[float] = mapped_column(default=0)
    master: Mapped["DbMaster"] = relationship("DbMaster", back_populates="rating", uselist=False)

    def __repr__(self):
        return f"Master with id = {self.master.id} has rating = {self.rating}"
