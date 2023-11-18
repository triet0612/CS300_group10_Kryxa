from typing import Annotated, Literal
from pydantic import BaseModel, Field
from db.database import DBService


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
                "SELECT PcID,Status FROM Pc "
            ).fetchall()
            for i in pc_info:
                list_Pc.append({'PcID': i[0], 'Status': i[1]})
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
            pc_info = Pc(PcID=pc_id,EndTime=pc[1],Password=pc[2],IPv4=pc[3],TimeUsage=pc[4])
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
                "INSERT INTO Pc VALUES (?, ?, ?, ?, 0, ?)",
                [new_pc.PcID, new_pc.Password, new_pc.MAC, new_pc.IPv4, new_pc.Status]
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            raise err
