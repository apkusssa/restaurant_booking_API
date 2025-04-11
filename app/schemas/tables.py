from enum import Enum

from pydantic import BaseModel, Field


class Location(str, Enum):
    window = "window"
    center = "center"
    corner = "corner"


class TableBase(BaseModel):
    name: str
    seats: int = Field(gt=0)
    location: Location

    class Config:
        orm_model = True


class TableCreate(TableBase):
    pass


class TableRead(TableBase):
    id: int
