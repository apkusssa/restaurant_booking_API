import datetime
from enum import Enum
from tkinter import CASCADE
from typing import Annotated

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


intpk = Annotated[int, mapped_column(primary_key=True)]

class Location(Enum):
    window = "window"
    terrace = "terrace"


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
    location: Mapped[Location]


class Reservayon(Base):
    __tablename__ = "бронь"
    
    id: Mapped[intpk]
    customer_name: Mapped[str] = mapped_column(
        nullable=False
    )
    table_id: Mapped[int] = mapped_column(
        ForeignKey("tables.id", ondelete=CASCADE)
    )
    reservation_time: Mapped[datetime.datetime] = mapped_column(
    )
    duration_minutes: Mapped[int]