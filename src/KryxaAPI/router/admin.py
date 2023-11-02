from fastapi import APIRouter, HTTPException, Response, Depends
from typing import Annotated

import model.PC
from auth import checkAdminAccount, generate_token, validateAdminToken, AccountDTO
import array as arr
from model.PC import Pc, fetch_pc_by_id, insert_pc

adminRouter = APIRouter(tags=["admin"])


# @adminRouter.get("/")
# async def home_admin(acc: Annotated[AccountDTO, Depends(validateAdminToken)]):
#     return {"message": "welcome admin ID: " + str(acc.ID)}


@adminRouter.post("/login")
async def login(acc: AccountDTO, res: Response) -> str:
    try:
        valid = checkAdminAccount(acc)
        if valid is False:
            raise HTTPException(status_code=401, detail="Wrong password or id")
        res.headers.append("Authorization", generate_token(acc))
        return "Login successful"
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail="Error validating")


@adminRouter.get("/{pc_id}")
async def fetch_pc_id(pc_id: int):
    try:
        pc_info = fetch_pc_by_id(pc_id)
        return pc_info
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail="No pc with that id")


@adminRouter.get("/")
async def view_pcs():
    list_pc = []
    try:
        list_pc = model.PC.fetch_All_Pcs()
        return list_pc
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail="Error validating")


@adminRouter.post("/pc", dependencies=[Depends(validateAdminToken)])
async def create_pc(new_pc: Pc):
    try:
        insert_pc(new_pc)
        return "Successfully create pc"
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error create Pc")
