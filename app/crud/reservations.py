from sqlalchemy.orm import Session
from app.models.reservations import ReservationOrm
from app.schemas.reservations import ReservationCreate

def get_all(db: Session):
    return db.query(ReservationOrm).all()

def create(db: Session, reservation: ReservationCreate):
    db_reservation = ReservationOrm(
        customer_name=reservation.customer_name,
        table_id=reservation.table_id,
        reservation_time=reservation.reservation_time,
        duration_minutes=reservation.duration_minutes
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def remove(db: Session, reservation_id: int):
    db.query(ReservationOrm).filter(ReservationOrm.id == reservation_id).delete()
    db.commit()
