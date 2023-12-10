import random
import sqlite3
from typing import Annotated, Literal

from fastapi import HTTPException
from pydantic import BaseModel, Field
from db.database import DBService
from datetime import datetime
from datetime import timedelta
import json


class Pc(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    EndTime: str
    Password: Annotated[str, Field(max_length=3, min_length=3)]
    IPv4: str
    TimeUsage: Annotated[int, Field(default=0)]


class PcDTO(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Password: Annotated[str, Field(max_length=3, min_length=3)]
    IPv4: str


# TODO: getAllPcsForView()

def fetch_All_Pcs():
    list_Pc = []
    with DBService() as cur:
        try:
            pc_info = cur.cursor().execute(
                "SELECT PcID,EndTime FROM Pc "
            ).fetchall()
            for i in pc_info:
                list_Pc.append({'PcID': i[0], 'EndTime': i[1]})
            return list_Pc
        except Exception as err:
            print(err)


# TODO: getPCbyID(id: int)
def fetch_pc_by_id(pc_id: int) -> Pc:
    with DBService() as cur:
        try:
            pc = cur.cursor().execute(
                "SELECT * FROM Pc WHERE PcId =?", [pc_id]
            ).fetchone()
            pc_info = Pc(PcID=pc_id, EndTime=pc[1], Password=pc[2], IPv4=pc[3], TimeUsage=pc[4])
            return pc_info
        except Exception as err:
            print(err)


# TODO: UpdatePCbyID(id: int)
def update_pc_by_id(pc_info: PcDTO) -> str:
    with DBService() as cur:
        try:
            cur.execute(
                "UPDATE Pc SET Password = ?, IPv4 = ? WHERE PcID = ?", [pc_info.Password, pc_info.IPv4, pc_info.PcID]
            )
            cur.commit()
            return pc_info.IPv4
        except Exception as err:
            cur.rollback()
            raise err


def insert_pc(new_pc: Pc):
    with DBService() as cur:
        try:
            cur.execute(
                "INSERT INTO Pc VALUES (?, ?, ?, ?, 0)",
                [new_pc.PcID, new_pc.EndTime, new_pc.Password, new_pc.IPv4]
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            raise err


def fetch_time_usage():
    pc_list = []
    time_usage_list = []
    with DBService() as cur:
        try:
            rows = cur.cursor().execute('SELECT "PcID", "TimeUsage" FROM "Pc"').fetchall()
            for r in rows:
                pc_list.append(r[0])
                time_usage_list.append(r[1])
            return {"pc_list": pc_list, "time_usage_list": time_usage_list}
        except sqlite3.Error as err:
            print(err)
            raise HTTPException(500, "Database error")


def start_session(pc_id: int, time_pack: int):
    with DBService() as cur:
        try:
            end_time = datetime.now() + timedelta(minutes=time_pack * 30)
            end_time = end_time.replace(microsecond=0)
            password = random.randrange(100, 999, 1)
            cur.execute(
                "UPDATE Pc SET EndTime=?, Password=? WHERE PcID=?",
                [end_time.isoformat(), password, pc_id]
            )
            item_price = cur.execute("SELECT Price FROM SaleItem WHERE ItemID=1").fetchone()
            cart = [{
                "Name": "Time package",
                "Number": time_pack,
                "Price": item_price[0]
            }]
            cur.execute(
                '''INSERT INTO "Bill" ("PcID", "Datetime", "Note", "Total", "Cart") VALUES(?, ?, ?, ?, ?)''',
                [pc_id, "", "", 0, json.dumps(cart)]
            )
            cur.commit()
        except sqlite3.Error as err:
            cur.rollback()
            raise err


def terminate_session(pc_id: int):
    with DBService() as cur:
        try:
            end_time = datetime.now()
            end_time = end_time.replace(microsecond=0)
            cur.execute(
                "UPDATE Pc SET EndTime=? WHERE PcID=?",
                [end_time.isoformat(), pc_id]
            )
            cur.execute(
                'DELETE FROM "Bill" WHERE "PcID" = ? AND "Datetime" = ""',
                [pc_id]
            )
            cur.commit()
        except sqlite3.Error as err:
            cur.rollback()
            raise err
