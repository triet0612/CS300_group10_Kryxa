from fastapi import APIRouter, HTTPException, Response, Depends
from typing import Annotated

import model.PC
from auth import checkAdminAccount, generate_token, validateAdminToken, AccountDTO
import array as arr
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


@adminRouter.get("/pc_status")
async def view_pcs():
    list_pc=[]
    try:
        list_pc=model.PC.fetch_All_Pcs()
        return list_pc
    except Exception as err:
        raise HTTPException(status_code=401, detail="Error validating")

