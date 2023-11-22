from datetime import datetime
from pydantic import BaseModel, Field, field_serializer
from typing import Annotated, Literal
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


def fetch_bill_byID(bill_id: int) -> Bill:
    with DBService() as cur:
        try:
            bill = cur.cursor().execute(
                "SELECT * FROM Bill WHERE BillID =?", [bill_id]
            ).fetchone()
            bill_info = Bill(BillID=bill[0], PcID=bill[1], Datetime=bill[2], Note=bill[3], Total=bill[4],
                             Cart=list(eval(bill[5])))
            print(bill_info)
            return bill_info
        except Exception as err:
            print(err)
