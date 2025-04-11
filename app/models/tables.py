from enum import Enum

from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, intpk


class Location(Enum):
    window = "window"
    center = "center"
    corner = "corner"


class TableOrm(Base):
    __tablename__ = "tables"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(
        nullable=False,
        unique=True
    )
    seats: Mapped[int] = mapped_column(
        nullable=False
    )
    location: Mapped[Location] = mapped_column(
        SqlEnum(Location),
        nullable=False
    )
