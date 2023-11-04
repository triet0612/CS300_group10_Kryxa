from pydantic import BaseModel, Field
from typing import Annotated, Literal, List, Dict, Any
from db.database import DBService


class SaleItems(BaseModel):
    ItemID: Annotated[int, Field(ge=0)]
    Name: Annotated[str, Field(max_length=20)]
    Price: float
    Category: Annotated[str, Field(max_length=20)]
    ItemStatus: Literal['Deprecated', 'On sale']
    Stock: Annotated[int, Field(ge=0)]


def fetch_all_items():
    with DBService() as cur:
        try:
            list_items = []
            items = cur.cursor().execute("SELECT * FROM SaleItem").fetchall()
            for x in items:
                list_items.append(
                    SaleItems(ItemID=x[0], Name=x[1], Price=x[2], Category=x[3], ItemStatus=x[4], Stock=x[5]))
            print(list_items)
            return list_items
        except Exception as err:
            print(err)


def fetch_items_id(itemid):
    with DBService() as cur:
        try:
            items = cur.cursor().execute("SELECT * FROM SaleItem where ItemID = ?", (itemid,)).fetchone()
            fetched = SaleItems(ItemID=itemid, Name=items[1], Price=items[2], Category=items[3], ItemStatus=items[4],
                                Stock=items[5])
            return fetched
        except Exception as err:
            print(err)
