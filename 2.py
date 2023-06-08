""" Models form the structures:
(declarative mappings: python object model -> database metadata)
which will be queryed from the database (books for our mission)

That metadata will serve as input along with the engine to create tables
"""

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    author: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(500))
    year_published: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, Title={self.title!r}, Author={self.author!r}, Description={self.description!r}, Year published={self.year_published!r})"