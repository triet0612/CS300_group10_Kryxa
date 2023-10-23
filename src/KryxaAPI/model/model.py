import datetime
from pydantic import BaseModel, Field
from typing import Annotated, Literal


class Bill(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Datetime: datetime.datetime
    AdminID: int
    Status: Literal['In progress', 'Completed', 'Denied']
    Note: Annotated[str, Field(max_length=100)]
    Total: Annotated[float, Field(default=0)]
    Cart: list[dict]


class Admin(BaseModel):
    AdminID: Annotated[int, Field(ge=0)]
    Fullname: Annotated[str, Field(max_length=100, min_length=1)]
    Phone: Annotated[str, Field(min_length=1)]
    Password: Annotated[str, Field(min_length=1)]
