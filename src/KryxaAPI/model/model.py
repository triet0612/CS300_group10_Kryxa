from pydantic import BaseModel, Field
from typing import Annotated, Literal


class Pc(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Password: Annotated[str, Field(max_length=3, min_length=3)]
    MAC: str
    IPv4: str
    TimeUsage: Annotated[int, Field(default=0)]


class SaleItems(BaseModel):
    ItemID: Annotated[int, Field(ge=0)]
    Name: Annotated[str, Field(max_length=20)]
    Price: float
    Category: Annotated[str, Field(max_length=20)]
    ItemStatus: Literal['Deprecated', 'On Sale']
    Stock: Annotated[int, Field(ge=0)]

