from typing import Annotated
import jwt
from pydantic import BaseModel, Field

from db.database import DBService
from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException
from model.Admin import Admin

HASH_ALGORITHM = 'HS256'
JWT_SECRET = 'secret'

jwt_auth = HTTPBearer(
    scheme_name='Authorization'
)


class AccountDTO(BaseModel):
    ID: Annotated[int, Field(ge=0)]
    Password: str

class ChangePassword(BaseModel):
    oldPassword:str
    newPassword:str

def generate_admin_token(acc: Admin) -> str:
    to_encode = {"Password": acc.Password}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=HASH_ALGORITHM)
    return encoded_jwt


def checkAdminAccount(acc: Admin) -> bool:
    with DBService() as cur:
        try:
            row = cur.cursor().execute("SELECT Password FROM Admin").fetchone()
            if acc.Password == row[0]:
                return True
            return False
        except Exception as err:
            cur.rollback()
            print(err)
            return False


def validateAdminToken(creds=Depends(jwt_auth)) -> Admin:
    try:
        payload = jwt.decode(creds.credentials, JWT_SECRET, algorithms=[HASH_ALGORITHM])
        acc = Admin(Password=payload["Password"])
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


def change_password(item:ChangePassword) -> bool:
    with DBService() as cur:
        try:
            row = cur.cursor().execute("SELECT Password FROM Admin").fetchone()
            if item.oldPassword != row[0]:
                return False
            cur.execute(
                "UPDATE Admin SET Password=?",
                [item.newPassword]
            )
            cur.commit()
            return True
        except Exception as err:
            cur.rollback()
            print(err)
