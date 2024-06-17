from sqlalchemy import ForeignKey

from dependencies.database.db import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from models.category_model import DbCategory

class DbService(Base):
    __tablename__ = "services"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    name: Mapped[str] = mapped_column()

    # Связь Many-to-One с категорией
    category: Mapped["DbCategory"] = relationship("DbCategory", back_populates='services')

    # Связь Many-to-One с ценой
    prices: Mapped[list["DbPrice"]] = relationship("DbPrice", back_populates='service')

    def __repr__(self):
        return f"{self.name}"
