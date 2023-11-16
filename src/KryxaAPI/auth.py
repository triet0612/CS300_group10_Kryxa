from typing import Annotated
import jwt
from pydantic import BaseModel, Field

from db.database import DBService
from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException

HASH_ALGORITHM = 'HS256'
JWT_SECRET = 'secret'

jwt_auth = HTTPBearer(
    scheme_name='Authorization'
)


class AccountDTO(BaseModel):
    ID: Annotated[int, Field(ge=0)]
    Password: str


def generate_token(acc: AccountDTO) -> str:
    to_encode = {
        "ID": acc.ID, "Password": acc.Password
    }
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=HASH_ALGORITHM)
    return encoded_jwt


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


def validateAdminToken(creds=Depends(jwt_auth)) -> AccountDTO:
    try:
        payload = jwt.decode(creds.credentials, JWT_SECRET, algorithms=[HASH_ALGORITHM])
        acc = AccountDTO(ID=payload["ID"], Password=payload["Password"])
        if not checkAdminAccount(acc):
            raise HTTPException(status_code=401, detail='Token unauthorized')
        return acc
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail='Error token')


def checkPcAccount(acc: AccountDTO) -> bool:
    with DBService() as cur:
        try:
            row = cur.cursor().execute(
                "SELECT Password FROM Pc WHERE PcID=?",
                [acc.ID]
            ).fetchone()
            if acc.Password == row[0]:
                return True
            return False
        except Exception as err:
            cur.rollback()
            print(err)
            return False


def validatePcToken(creds=Depends(jwt_auth)) -> AccountDTO:
    try:
        payload = jwt.decode(creds.credentials, JWT_SECRET, algorithms=[HASH_ALGORITHM])
        acc = AccountDTO(ID=payload["ID"], Password=payload["Password"])
        if not checkPcAccount(acc):
            raise HTTPException(status_code=401, detail='Token unauthorized')
        return acc
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail='Error token')
