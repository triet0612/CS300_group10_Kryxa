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

class SaleItems(BaseModel):
    ItemID: Annotated[int, Field(ge = 0)]
    Name: Annotated[str, Field(max_length=20)]
    Price: Annotated[float, Field(ge=1000)]
    Category: Annotated[str, Field(max_length=20)]
    ItemStatus: Literal['Deprecated','On Sale']
    Stock: Annotated[int, Field(ge = 0)]