from fastapi import APIRouter, HTTPException, Response, Depends
from typing import Annotated
from auth import checkAdminAccount, generate_token, validateAdminToken
from model.model import AccountDTO

adminRouter = APIRouter(tags=["admin"])


@adminRouter.get("/")
async def home_admin(acc: Annotated[AccountDTO, Depends(validateAdminToken)]):
    print(acc)
    return {
        "message": "welcome admin ID: " + str(acc.ID),
    }


@adminRouter.post("/login")
async def login(acc: AccountDTO, res: Response) -> str:
    try:
        valid = checkAdminAccount(acc)
        if valid is False:
            raise HTTPException(status_code=401, detail="Wrong password or id")
        res.headers.append("Authorization", generate_token(acc))
        return "Logined"
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail="Error validating")
