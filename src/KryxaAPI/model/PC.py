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

<<<<<<< Updated upstream
#TODO: getAllPcsForView()

=======

# TODO: getAllPcsForView()
>>>>>>> Stashed changes
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


<<<<<<< Updated upstream
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

#TODO: getPCbyID(id: int)
a = fetch_All_Pcs()
print(a)

=======
# # TODO: getPCbyID(id: int)
# a = fetch_All_Pcs()
# print(a)
>>>>>>> Stashed changes
