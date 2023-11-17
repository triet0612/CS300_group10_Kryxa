from pydantic import BaseModel, Field
from typing import Annotated, Literal
from db.database import DBService


class SaleItems(BaseModel):
    ItemID: Annotated[int, Field(ge=0)]
    Name: Annotated[str, Field(max_length=20)]
    Price: float
    Category: Annotated[str, Field(max_length=20)]
    Stock: Annotated[int, Field(ge=0)]


def fetch_all_items():
    sql_query: str = "SELECT * FROM SaleItem"

    with DBService() as cur:
        items = cur.cursor().execute(sql_query).fetchall()  # Row objects fetched
        item_list = []
        for item_row in items:  # Convert Row objects to SaleItems objects
            item_list.append(SaleItems(ItemID=item_row[0],
                                       Name=item_row[1],
                                       Price=item_row[2],
                                       Category=item_row[3],
                                       Stock=item_row[4]))
        return item_list


def fetch_items_id(itemid: int):
    with DBService() as cur:
        try:
            items = cur.cursor().execute("SELECT * FROM SaleItem where ItemID = ?", (itemid,)).fetchone()
            fetched = SaleItems(ItemID=items[0],
                                Name=items[1],
                                Price=items[2],
                                Category=items[3],
                                Stock=items[4])
            return fetched
        except Exception as err:
            print(err)


def create_item(item: SaleItems):
    with DBService() as cur:
        try:
            cur.cursor().execute("INSERT INTO SaleItem VALUES (?,?,?,?,?)",
                                 (item.ItemID, item.Name, item.Price, item.Category, item.Stock,))
            cur.commit()
        except Exception as err:
            cur.rollback()
            raise err


def update_item(new_item_data: SaleItems):
    sql_query: str = "UPDATE SaleItem SET Name = ?, Price = ?, Category = ?, ItemStatus = ?, Stock = ? WHERE ItemID = ?"

    with DBService() as cur:
        try:
            cur.cursor.execute(sql_query,
                               new_item_data.Name,
                               new_item_data.Price,
                               new_item_data.Category,
                               new_item_data.ItemStatus,
                               new_item_data.Stock
                               )
        except Exception as err:
            print(err)
