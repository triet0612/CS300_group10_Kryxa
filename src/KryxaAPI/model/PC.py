from typing import Annotated, Literal
from pydantic import BaseModel, Field
from db.database import DBService

class Pc(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Password: Annotated[str, Field(max_length=3, min_length=3)]
    MAC: str
    IPv4: str
    TimeUsage: Annotated[int, Field(default=0)]
    Status: Literal['Available', 'Unavailable']


# TODO: getAllPcsForView()
def fetch_All_Pcs():
    with DBService() as cur:
        try:
            view_Pc_info = cur.cursor().execute(
             "SELECT PcID, Status FROM Pc "
            ).fetchall()
            return view_Pc_info
            # for r in rows:
            #     Pc.append(Pc(PcID=r[0], Status=r[1]))
        except Exception as err:
            print(err)


# TODO: getPCbyID(id: int)
def fetch_pc_by_id(pc_id: int) -> Pc:
    with DBService() as cur:
        try:
            pc = cur.cursor().execute(
                "SELECT * FROM Pc WHERE PcId =?", [pc_id]
            ).fetchone()
            pc_info = Pc(PcID=pc_id,Password='123',MAC='',IPv4='',TimeUsage=0,Status='Available')
            pc_info.Password = pc[1]
            pc_info.MAC = pc[2]
            pc_info.IPv4 = pc[3]
            pc_info.TimeUsage = pc[4]
            pc_info.Status = pc[5]
            return pc_info
        except Exception as err:
            print(err)

