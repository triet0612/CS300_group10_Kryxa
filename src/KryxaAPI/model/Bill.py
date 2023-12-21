import json
import sqlite3
from datetime import datetime
from typing import Annotated, List

from fastapi import HTTPException
from pydantic import BaseModel, Field, field_serializer
from typing import Annotated, Literal
from db.database import DBService


class Bill(BaseModel):
    BillID: Annotated[int, Field(ge=0)]
    PcID: Annotated[int, Field(ge=0)]
    Datetime: datetime | None
    Note: Annotated[str, Field(max_length=100)]
    Total: Annotated[float, Field(default=0)]
    Cart: list[dict]

    @field_serializer('Datetime')
    def serialize_datetime(self, d: datetime):
        if d is not None:
            return d.astimezone().isoformat()
        else:
            return None


def fetch_bill_by_id(bill_id: int) -> list[Bill]:
    with DBService() as cur:
        try:
            bill_info = []
            bill = cur.cursor().execute(
                "SELECT * FROM Bill WHERE BillID =?", [bill_id]
            ).fetchone()
            bill_info.append(Bill(BillID=bill[0], PcID=bill[1], Datetime=bill[2], Note=bill[3], Total=bill[4],
                                  Cart=list(eval(bill[5]))))
            return bill_info
        except Exception as err:
            print(err)


def fetch_all_bills():
    sql_query: str = "SELECT * FROM Bill"
    with DBService() as cur:
        items = cur.cursor().execute(sql_query).fetchall()  # Row objects fetched
        item_list = []
        for item_row in items:  # Convert Row objects to SaleItems objects
            if item_row[2] != "":
                item_list.append(
                    Bill(BillID=item_row[0], PcID=item_row[1], Datetime=item_row[2], Note=item_row[3], Total=item_row[4],
                         Cart=list(eval(item_row[5]))), )
            else:
                item_list.append(
                    Bill(BillID=item_row[0], PcID=item_row[1], Datetime=None, Note=item_row[3],
                         Total=item_row[4],
                         Cart=list(eval(item_row[5]))), )
        return item_list


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


def update_bill(new_bill_data: Bill):
    with DBService() as cur:
        try:
            for item in new_bill_data.Cart:
                new_bill_data.Total += item["qt"] * item["price"]
            cart_json = json.dumps(new_bill_data.Cart)

            cur.cursor().execute(
                "UPDATE Bill SET Datetime = ?, Note = ?, Total = ?, Cart = ? WHERE BillID = ?",
                (new_bill_data.Datetime.isoformat(), new_bill_data.Note, new_bill_data.Total, cart_json, new_bill_data.BillID)
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)


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


def fetch_bill_by_pc_id(pc_id: int) -> Bill:
    with DBService() as cur:
        try:
            bill = cur.cursor().execute(
                'SELECT * FROM "Bill" WHERE "PcID" = ? AND "Datetime" = ""', [pc_id]
            ).fetchone()
            bill_info = Bill(BillID=bill[0], PcID=bill[1], Datetime=None, Note=bill[3], Total=bill[4],
                             Cart=list(eval(bill[5])))
            return bill_info
        except Exception as err:
            print(err)

def update_user_bill(new_bill_data: Bill):
    with DBService() as cur:
        try:
            total = 0
            print(new_bill_data.Cart)
            for item in new_bill_data.Cart:
                total += item["qt"] * item["price"]
            new_bill_data.Total = total
            cart_json = json.dumps(new_bill_data.Cart)

            cur.cursor().execute(
                "UPDATE Bill SET Note = ?, Total = ?, Cart = ? WHERE BillID = ?",
                (new_bill_data.Note, new_bill_data.Total, cart_json, new_bill_data.BillID)
            )
            cur.commit()
            print(new_bill_data)
        except Exception as err:
            cur.rollback()
            print(err)
