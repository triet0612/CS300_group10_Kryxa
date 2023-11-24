import sqlite3
from datetime import datetime
from pydantic import BaseModel, Field, field_serializer
from typing import Annotated, Literal
from db.database import DBService
from fastapi import HTTPException


class Bill(BaseModel):
    BillID: Annotated[int, Field(ge=0)]
    PcID: Annotated[int, Field(ge=0)]
    Datetime: datetime | None
    Note: Annotated[str, Field(max_length=100)]
    Total: Annotated[float, Field(default=0)]
    Cart: list[dict]

    @field_serializer('Datetime')
    def serialize_datetime(self, d: datetime):
        return d.astimezone().isoformat()


def fetchSalesByMonth(month, year):
    sales_list = []
    month_list = []
    with (DBService() as cur):
        try:
            rows = cur.cursor().execute(
                '''SELECT date("Datetime") as "day", sum("Total") as "sales" FROM "Bill"
WHERE strftime('%m', "Datetime") = ? 
AND strftime('%Y', "Datetime") = ?
GROUP BY strftime('%d', "Datetime")''', [str(month), str(year)]
            ).fetchall()
            for r in rows:
                sales_list.append(int(r[1]))
                month_list.append(r[0])
            return {"sales": sales_list, "month": month_list}
        except sqlite3.Error as err:
            print(err)
            raise HTTPException(500, "Database error")


def fetchSalesByPcID():
    sales_list = []
    pc_list = []
    with (DBService() as cur):
        try:
            rows = cur.cursor().execute('SELECT "PcID", sum("Total") as "Sales" FROM "Bill" GROUP BY "PcID"').fetchall()
            for r in rows:
                pc_list.append(r[0])
                sales_list.append(int(r[1]))
            return {"sales": sales_list, "pc_list": pc_list}
        except sqlite3.Error as err:
            print(err)
            raise HTTPException(500, "Database error")


def checkBillRequireConfirm():
    with DBService() as cur:
        try:
            rows = cur.cursor().execute(
                '''SELECT EndTime FROM (
    SELECT PcID, BillID FROM Bill
    WHERE "Datetime" = ""
) b JOIN Pc p ON b.PcID = p.PcID
''').fetchall()
            for r in rows:
                temp_date = datetime.fromisoformat(r[0])
                if datetime.now() > temp_date:
                    return True
            return False
        except sqlite3.Error as err:
            print(err)
            raise HTTPException(500, "Database error")
