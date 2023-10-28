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


#TODO: getAllPcsForView()
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

#TODO: getPCbyID(id: int)
