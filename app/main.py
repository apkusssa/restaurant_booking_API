from fastapi import FastAPI

from app.api.v1 import tables, reservations
from app.db.session import sync_engine
from app.db.base import Base


Base.metadata.create_all(bind=sync_engine)


app = FastAPI(title="Restaurant Booking API")

app.include_router(tables.router, prefix="/api/v1/tables")
app.include_router(reservations.router, prefix="/api/v1/reservations")
