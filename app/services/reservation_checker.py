from sqlalchemy.orm import Session
from app.models.reservations import ReservationOrm
import datetime

def is_time_slot_available(db: Session, table_id: int, reservation_time: datetime, duration_minutes: int):
    end_time = reservation_time + datetime.timedelta(minutes=duration_minutes)
    conflicting_reservation = db.query(ReservationOrm).filter(
        ReservationOrm.table_id == table_id,
        ReservationOrm.reservation_time < end_time,
        ReservationOrm.reservation_time + datetime.timedelta(minutes=ReservationOrm.duration_minutes) > reservation_time
    ).first()
    return conflicting_reservation is None
