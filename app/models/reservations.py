import datetime
from tkinter import CASCADE

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, intpk


class ReservationOrm(Base):
    __tablename__ = "reservations"
    
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
