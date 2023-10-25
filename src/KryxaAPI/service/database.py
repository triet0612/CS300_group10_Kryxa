from datetime import datetime
import json
import sqlite3
from model.model import Bill


class DBService:
    def __init__(self, path='../bin/test.db'):
        self.path = path
        self.con: sqlite3.Connection

    def __enter__(self):
        self.con = sqlite3.connect(self.path)
        self.con.serialize()
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con:
            self.con.close()


def fetchBillList() -> list[Bill]:
    with DBService() as cur:
        try:
            bill: list[Bill] = []
            rows = cur.execute("SELECT * FROM Bill")
            for row in rows.fetchall():
                bill.append(Bill(
                    PcID=row[0], Datetime=datetime.fromisoformat(row[1]),
                    AdminID=row[2], Status=row[3], Note=str(row[4]),
                    Total=row[5], Cart=json.loads(row[6])
                ))
            return bill
        except Exception as error:
            print(error)
            return []


def insertBill(newBill: Bill):
    with DBService() as cur:
        try:
            cur.execute(
                "INSERT INTO Bill VALUES (:PcID, :Datetime, :AdminID, :Status, :Note, :Total, :Cart)",
                newBill.model_dump()
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)


def deleteBill(PcID: int, Datetime: datetime):
    with DBService() as cur:
        try:
            cur.execute(
                "DELETE FROM Bill WHERE PcID=? AND Datetime=?",
                [PcID, Datetime.astimezone().isoformat()]
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)


def updateBill(changedBill: Bill):
    with DBService() as cur:
        try:
            cur.execute(
                "UPDATE Bill SET AdminID=:AdminID, Status=:Status, Note=:Note, Total=:Total, Cart=:Cart"
                "WHERE PcID==:PcID AND Datetime==:Datetime",
                changedBill.model_dump()
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)
