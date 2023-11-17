import random
import sqlite3
from typing import Annotated, Literal
from pydantic import BaseModel, Field
from db.database import DBService
from datetime import datetime
from datetime import timedelta


class Pc(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    EndTime: str
    Password: Annotated[str, Field(max_length=3, min_length=3)]
    IPv4: str
    TimeUsage: Annotated[int, Field(default=0)]


class PcDTO(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Status: Literal['Available', 'Unavailable', 'Maintenance']


# TODO: getAllPcsForView()

def fetch_All_Pcs():
    list_pc = []
    with DBService() as cur:
        try:
            pc_info = cur.cursor().execute(
                "SELECT PcID, EndTime FROM Pc"
            ).fetchall()
            for i in pc_info:
                pc_id = i[0]
                end_time = i[1]
                status = "Unavailable"
                if datetime.fromisoformat(end_time) < datetime.now():
                    status="Available"
                list_pc.append(PcDTO(PcID=pc_id, Status=status))
            return list_pc
        except Exception as err:
            print(err)


# TODO: getPCbyID(id: int)
def fetch_pc_by_id(pc_id: int) -> Pc:
    with DBService() as cur:
        try:
            pc = cur.cursor().execute(
                "SELECT * FROM Pc WHERE PcId =?", [pc_id]
            ).fetchone()
            pc_info = Pc(PcID=pc_id, Password=pc[1], MAC=pc[2], IPv4=pc[3], TimeUsage=pc[4], Status=pc[5])
            return pc_info
        except Exception as err:
            print(err)


# TODO: UpdatePCbyID(id: int)
# def update_pc_by_id(pc_info: PcDTO) -> str:
#     with DBService() as cur:
#         try:
#             cur.execute(
#                 "UPDATE Pc SET MAC = ?, IPv4 = ? WHERE PcID = ?", [pc_info.MAC, pc_info.IPv4, pc_info.PcID]
#             )
#             cur.commit()
#             return pc_info.IPv4
#         except Exception as err:
#             cur.rollback()
#             raise err

def insert_pc(new_pc: Pc):
    with DBService() as cur:
        try:
            cur.execute(
                "INSERT INTO Pc VALUES (?, ?, ?, ?, 0, ?)",
                [new_pc.PcID, new_pc.Password, new_pc.MAC, new_pc.IPv4, new_pc.Status]
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            raise err


def start_session(pc_id: int, time_pack: int):
    with DBService() as cur:
        try:
            end_time = datetime.now() + timedelta(minutes=time_pack * 30)
            password = random.randrange(100, 999, 1)
            cur.execute(
                "UPDATE Pc SET EndTime=?, Password=? WHERE PcID=?",
                [end_time.isoformat(), password, pc_id]
            )
            cur.execute(
                '''INSERT INTO "Bill" ("PcID", "Datetime", "Note", "Total", "Cart") VALUES(?, ?, ?, ?, ?)''',
                [pc_id, "", "", 0, "[]"]
            )
            cur.commit()
        except sqlite3.Error as err:
            cur.rollback()
            raise err
