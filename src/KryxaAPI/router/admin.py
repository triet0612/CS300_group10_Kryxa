from fastapi import APIRouter, HTTPException, Response, Depends, File
from typing import Annotated

import model.PC
from auth import checkAdminAccount, generate_token, validateAdminToken, AccountDTO
import model.SaleItems
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


@adminRouter.get("/items", dependencies=[Depends(validateAdminToken)])
async def get_all_items(item_name: str | None = None, item_category: str | None = None):
    try:
        item_list = model.SaleItems.fetch_all_items()
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


# track info for each item id
@adminRouter.get("/items/{item_id}", dependencies=[Depends(validateAdminToken)])
async def read_item(item_id: int):
    try:
        item = model.SaleItems.fetch_items_id(item_id)
        if item:
            return item
        raise Exception(FileNotFoundError)
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, details="Error not found")


# create item and image file
@adminRouter.post("/get_items", dependencies=[Depends(validateAdminToken)])
async def create_item(item: model.SaleItems.SaleItems, file: Annotated[bytes, File()]):
    return item, file


@adminRouter.get("/{pc_id}", dependencies=[Depends(validateAdminToken)])
async def fetch_pc_id(pc_id: int):
    try:
        pc_info = fetch_pc_by_id(pc_id)
        return pc_info
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail="No pc with that id")


@adminRouter.get("/", dependencies=[Depends(validateAdminToken)])
async def view_pcs():
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
