import sqlite3
from io import BytesIO

from service.file import get_file

from fastapi import APIRouter, Response, HTTPException, Depends
from fastapi.responses import StreamingResponse
from auth import AccountDTO, checkPcAccount, generate_pc_token, validatePcToken
from typing import Annotated
from model.SaleItems import SaleItems, fetch_all_items
from model.PC import fetch_pc_by_id

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


@userRouter.get("/items", dependencies=[Depends(validatePcToken)])
async def get_all_items(item_name: str | None = None, item_category: str | None = None):
    try:
        item_list = fetch_all_items()
        if len(item_list) == 0:
            raise HTTPException(status_code=404,
                                detail="No items")  # This should not be 404, should have a notification screen

        if item_category:
            item_list[:] = [item for item in item_list if item.Category == item_category]

        if item_name:
            item_list[:] = [item for item in item_list if item_name in item.Name]

        return item_list

    except HTTPException:
        pass  # ignore HTTPException


@userRouter.get("/time")
async def get_time_remaining(acc: Annotated[AccountDTO, Depends(validatePcToken)]):
    try:
        pc = fetch_pc_by_id(acc.PcID)
        return {"EndTime": pc.EndTime}
    except HTTPException as err:
        raise err
    except sqlite3.Error as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error fetching time")
    except Exception as err:
        raise HTTPException(status_code=500, detail="Unknown error")


file_manager = get_file()
@userRouter.get("/getfile/{filename}")
async def get_file(filename: int):
    try:
        # Read the image using FileManager
        image_byte_stream = file_manager.read_image(filename)
        # Return the image as a streaming response
        return StreamingResponse(BytesIO(image_byte_stream), media_type="image/jpeg")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
