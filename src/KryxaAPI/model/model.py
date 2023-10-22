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


class Pc(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Password: Annotated[str, Field(max_length=3)]
    MAC: str
    IPv4: str
    TimeUsage: Annotated[int, Field(default=0)]



