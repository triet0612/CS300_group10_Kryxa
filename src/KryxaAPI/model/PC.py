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
    list_Pc=[]
    with DBService('../bin/kryxa.db') as cur:
        try:
            pc_info = cur.cursor().execute(
             "SELECT PcID,Status FROM Pc "
            ).fetchall()
            for i in pc_info:
                list_Pc.append({'PcID':i[0], 'Status':i[1]})
            return list_Pc
        except Exception as err:
            print(err)


#TODO: getPCbyID(id: int)
a = fetch_All_Pcs()
print(a)