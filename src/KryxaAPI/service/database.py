from datetime import datetime
import json
import sqlite3
from model.model import Bill, AccountDTO
from model.model import SaleItems


class DBService:
    def __init__(self, path='./bin/test.db'):
        self.path = path
        self.con: sqlite3.Connection

    def __enter__(self):
        self.con = sqlite3.connect(self.path)
        return self.con

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.con:
            self.con.close()

#Bill 
def fetchBillList() -> list[Bill]:
    with DBService() as cur:
        try:
            bill: list[Bill] = []
            rows = cur.cursor().execute("SELECT * FROM Bill")
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
#SaleItems 
def fetchItem()->list[SaleItems]:
    with DBService() as cur:
        try:
            items: list[SaleItems] = []
            rows = cur.cursor().execute("SELECT * FROM SaleItems")
            for row in rows.fetchall():
                items.append(SaleItems(
                    ItemID=row[0], Name= str(row[1]),
                    Price=float(row[2]), Category=str(row[3]),
                    ItemStatus=row[4],Stock=row[5]
                ))
            return items
        except Exception as error:
            print(error)
            return []

def insertItem(newItem:SaleItems):
    with DBService() as cur:
        try:
            cur.execute(
                "INSERT INTO SaleItems VALUES (:ItemID, :Name, :Price, :Category, :ItemStatus, :Stock)",
                newItem.model_dump()
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)

def deleteItem(ItemID: int):
    with DBService() as cur:
        try:
            cur.execute(
                "DELETE FROM SaleItems WHERE ItemID=?",
                [ItemID]
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)


def updateItem(changedItem: SaleItems):
    with DBService() as cur:
        try:
            cur.execute(
                "UPDATE SaleItems SET ItemID=:ItemID, Name=:Name, Price=:Price, Category=:Category, ItemStatus=:ItemStatus, Stock=:Stock"
                "WHERE ItemID==:ItemID",
                changedItem.model_dump()
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)

#login logic
def checkAdminAccount(acc: AccountDTO) -> bool:
    with DBService() as cur:
        try:
            row = cur.cursor().execute(
                "SELECT Password FROM Admin WHERE AdminID=?",
                [acc.ID]
            ).fetchone()
            if acc.Password == row[0]:
                return True
            return False
        except Exception as err:
            cur.rollback()
            print(err)
            return False
