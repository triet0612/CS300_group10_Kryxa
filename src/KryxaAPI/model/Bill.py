import json
from datetime import datetime
from pydantic import BaseModel, Field, field_serializer
from typing import Annotated
from db.database import DBService


class Bill(BaseModel):
    BillID: Annotated[int, Field(ge=0)]
    PcID: Annotated[int, Field(ge=0)]
    Datetime: datetime
    Note: Annotated[str, Field(max_length=100)]
    Total: Annotated[float, Field(default=0)]
    Cart: list[dict]

    @field_serializer('Datetime')
    def serialize_datetime(self, d: datetime):
        return d.astimezone().isoformat()


def fetch_all_bills():
    sql_query: str = "SELECT * FROM Bill"
    with DBService() as cur:
        items = cur.cursor().execute(sql_query).fetchall()  # Row objects fetched
        item_list = []
        for item_row in items:  # Convert Row objects to SaleItems objects
            item_list.append(
                Bill(BillID=item_row[0], PcID=item_row[1], Datetime=item_row[2], Note=item_row[3], Total=item_row[4],
                     Cart=list(eval(item_row[5]))),)
        return item_list
