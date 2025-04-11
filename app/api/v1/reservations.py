from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.reservations import ReservationCreate, ReservationRead
from app.crud import reservations as crud_reservations
from app.db.session import get_db
from app.services.reservation_checker import is_time_slot_available

router = APIRouter(prefix="/reservations", tags=["reservations"])


@router.get("/", response_model=list[ReservationRead])
def read_reservations(db: Session = Depends(get_db)):
    return crud_reservations.get_all(db)


@router.post("/", response_model=ReservationRead)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    if not is_time_slot_available(db, reservation.table_id, reservation.reservation_time, reservation.duration_minutes):
        raise HTTPException(status_code=400, detail="Time slot is not available")
    return crud_reservations.create(db, reservation)


@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    if not crud_reservations.get(db, reservation_id):
        raise HTTPException(status_code=404, detail="Reservation not found")
    crud_reservations.remove(db, reservation_id)
    return {"ok": True}
