from typing import Annotated
from pydantic import BaseModel, Field
from db.database import DBService


class Pc(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    Password: Annotated[str, Field(max_length=3, min_length=3)]
    MAC: str
    IPv4: str
    TimeUsage: Annotated[int, Field(default=0)]


def insert_pc(new_pc: Pc):
    with DBService() as cur:
        try:
            cur.execute(
                "INSERT INTO Pc VALUES (?, ?, ?, ?, 0)",
                [new_pc.PcID, new_pc.Password, new_pc.MAC, new_pc.IPv4]
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            raise err
