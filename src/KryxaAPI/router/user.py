from fastapi import APIRouter, Response, HTTPException, Depends
from auth import AccountDTO, checkPcAccount, generate_pc_token, validatePcToken
from typing import Annotated

userRouter = APIRouter(tags=["user"])


@userRouter.get("/")
async def home_user():
    return "Home User"


@userRouter.post("/login")
async def login(acc: AccountDTO, res: Response) -> str:
    try:
        valid = checkPcAccount(acc)
        if valid is False:
            raise HTTPException(status_code=401, detail="Wrong password or id")
        res.headers.append("Authorization", generate_pc_token(acc))
        return "Login successful"
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail="Error validating")


@userRouter.get("/account")
async def get_acc(acc: Annotated[AccountDTO, Depends(validatePcToken)]):
    """
    NOTE: How to get account from JWT
    PLEASE USE THIS TO GET ACCOUNT OF CURRENT PC
    """
    print(acc)
    return acc
