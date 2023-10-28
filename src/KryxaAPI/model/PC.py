from typing import Annotated, Literal
from pydantic import BaseModel, Field
from db.database import DBService

class Pc(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Password: Annotated[str, Field(max_length=3, min_length=3)]
    MAC: str
    IPv4: str
    TimeUsage: Annotated[int, Field(default=0)]

class PcDTO(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Status: Literal['In progress', 'Completed', 'Denied']


#TODO: getAllPcs()
@Pc.get("/Pcs")
async def get_All_Pcs():
    Pcs = []
    with DBService() as cur:
        try:
            rows = cur.cursor().execute(
             "SELECT PcID, Status FROM Pc LEFT JOIN Bill ON Pc.PcID=Bill.PcID WHERE Bill.Status='In progress'"
            ).fetchall()
            for r in rows:
                Pcs.append(PcDTO(PcID=r[0], Status=r[1]))
        except Exception as err:
            print(err)

#TODO: getPCbyID(id: int)
