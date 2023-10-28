
from pydantic import BaseModel, Field
from typing import Annotated, Literal
class SaleItems(BaseModel):
    ItemID: Annotated[int, Field(ge = 0)]
    Name: Annotated[str, Field(max_length=20)]
    Price: float
    Category: Annotated[str, Field(max_length=20)]
    ItemStatus: Literal['Deprecated','On Sale']
    Stock: Annotated[int, Field(ge = 0)]