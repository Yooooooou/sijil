from sqlalchemy.orm import Mapped, mapped_column, relationship

from dependencies.database.db import Base


class DbCategory(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(unique=True, index=True)
    services: Mapped[list["DbService"]] = relationship("DbService", back_populates="category")

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name})"
