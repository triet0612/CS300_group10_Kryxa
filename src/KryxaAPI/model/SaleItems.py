from pydantic import BaseModel, Field
from typing import Annotated, Literal
from db.database import DBService


class SaleItems(BaseModel):
    ItemID: Annotated[int, Field(ge=0)]
    Name: Annotated[str, Field(max_length=20)]
    Price: float
    Category: Annotated[str, Field(max_length=20)]
    ItemStatus: Literal['Deprecated', 'On sale']
    Stock: Annotated[int, Field(ge=0)]


def fetch_all_items(item_name: str | None = None, item_category: str | None = None):
    sql_query: str = "SELECT * FROM SaleItem"

    with DBService() as cur:
        items = cur.cursor().execute(sql_query).fetchall()  # Row objects fetched
        item_list = []
        for item_row in items: # Convert Row objects to SaleItems objects
            item_list.append(SaleItems(ItemID=item_row[0],
                                       Name=item_row[1],
                                       Price=item_row[2],
                                       Category=item_row[3],
                                       ItemStatus=item_row[4],
                                       Stock=item_row[5]))
        return item_list


def fetch_items_id(itemid: int):
    with DBService() as cur:
        try:
            items = cur.cursor().execute("SELECT * FROM SaleItem where ItemID = ?", (itemid,)).fetchone()
            fetched = SaleItems(ItemID=itemid, Name=items[1], Price=items[2], Category=items[3], ItemStatus=items[4],
                                Stock=items[5])
            return fetched
        except Exception as err:
            print(err)


def create_item(item: SaleItems):
    with DBService() as cur:
        try:
            cur.cursor().execute("INSERT INTO SaleItem VALUES (?,?,?,?,?,?)",
                                 (item.ItemID, item.Name, item.Price, item.Category, item.ItemStatus, item.Stock,))
        except Exception as err:
            print(err)
