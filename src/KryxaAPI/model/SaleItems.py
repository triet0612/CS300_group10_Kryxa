from pydantic import BaseModel, Field
from typing import Annotated, Literal
from db.database import DBService


class SaleItems(BaseModel):
    ItemID: Annotated[int, Field(ge=0)]
    Name: Annotated[str, Field(max_length=20)]
    Price: float
    Category: Annotated[str, Field(max_length=20)]
    ItemStatus: Literal['Deprecated', 'On Sale']
    Stock: Annotated[int, Field(ge=0)]


def fetch_all_items():
    with DBService('../bin/kryxa.db') as cur:
        items = cur.cursor().execute("SELECT * FROM SaleItem").fetchall()
        return items


def fetch_items_id(itemid):
    with DBService('../bin/kryxa.db') as cur:
        items = cur.cursor().execute("SELECT * FROM SaleItem where ItemID = ?", itemid).fetchall()
        return items
