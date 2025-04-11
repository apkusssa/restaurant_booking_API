from sqlalchemy.orm import Session
from app.models.tables import TableOrm
from app.schemas.tables import TableCreate

def get_all(db: Session):
    return db.query(TableOrm).all()

def get_by_name(db: Session, name: str):
    return db.query(TableOrm).filter(TableOrm.name == name).first()

def create(db: Session, table: TableCreate):
    db_table = TableOrm(name=table.name, seats=table.seats, location=table.location)
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

def remove(db: Session, table_id: int):
    db.query(TableOrm).filter(TableOrm.id == table_id).delete()
    db.commit()
