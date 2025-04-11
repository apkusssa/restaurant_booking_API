from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tables import TableCreate, TableRead
from app.crud import tables as crud_tables
from app.db.session import get_db

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/", response_model=list[TableRead])
def read_tables(db: Session = Depends(get_db)):
    return crud_tables.get_all(db)

@router.post("/", response_model=TableRead)
def create_table(table: TableCreate, db: Session = Depends(get_db)):
    if crud_tables.get_by_name(db, table.name):
        raise HTTPException(status_code=400, detail="Table with this name already exists")
    return crud_tables.create(db, table)

@router.delete("/{table_id}")
def delete_table(table_id: int, db: Session = Depends(get_db)):
    if not crud_tables.get(db, table_id):
        raise HTTPException(status_code=404, detail="Table not found")
    crud_tables.remove(db, table_id)
    return {"ok": True}
