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


def fetch_all_items(item_name: str | None = None, item_category: str | None = None):
    """
    Returns a list of all SaleItems with optional filtering parameters if specified.
    :param item_name: filtered items Name contains this string
    :param item_category: filtered items Category equals to this string.
    :return: list of all SaleItems
    """
    sql_query: str = "SELECT * FROM SaleItems"
    sql_params = ()
    if item_name:  # items whose Name containing the string item_name
        sql_query += " WHERE Name LIKE %?% "
        sql_params = sql_params + (item_name,)
        if item_category:  # items belong to the Category is item_category
            sql_query += " AND WHERE Category = ?"
            sql_params = sql_params + (item_category,)

    if item_category:  # items belong to the Category is item_category
        sql_query += " WHERE Category = ?"
        sql_params = sql_params + (item_category,)
    sql_query += ";"
    with DBService() as cur:
        items = cur.cursor().execute(sql_query, sql_query).fetchall()  # Row objects fetched
        item_list = []
        for item_row in items: # Convert Row objects to SaleItems objects
            item_list.append(SaleItems(ItemID=item_row[0],
                                       Name=item_row[1],
                                       Price=item_row[2],
                                       Category=item_row[3],
                                       ItemStatus=item_row[4],
                                       Stock=item_row[5]))
        return item_list


def fetch_items_id(itemid):
    with DBService() as cur:
        items = cur.cursor().execute("SELECT * FROM SaleItem where ItemID = ?", (itemid,)).fetchall()
        return items
