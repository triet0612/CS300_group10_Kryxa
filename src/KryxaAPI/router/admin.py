from fastapi import APIRouter, HTTPException, Response, Depends, File
from typing import Annotated
from auth import checkAdminAccount, generate_token, validateAdminToken, AccountDTO
import model.SaleItems

adminRouter = APIRouter(tags=["admin"])


@adminRouter.get("/")
async def home_admin(acc: Annotated[AccountDTO, Depends(validateAdminToken)]):
    return {"message": "welcome admin ID: " + str(acc.ID)}


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


@adminRouter.get("/items")
async def get_all_items(item_name: str | None = None, item_category: str | None = None):
    try:
        item_list = model.SaleItems.fetch_all_items(item_name, item_category)
        if len(item_list) == 0:
            raise HTTPException(status_code=404,
                                detail="No items")  # This should not be 404, should have a notification screen
        return item_list
    except HTTPException:
        pass  # ignore HTTPException


# track info for each item id
@adminRouter.get("/items/{item_id}")
async def read_item(item_id: int):
    try:
        item = model.SaleItems.fetch_items_id(item_id)
        if item:
            return item
        raise HTTPException(status_code=404, detail="Item id does not exist")
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail="Item id does not exist")


# create item and image file
@adminRouter.post("/get_items")
async def create_item(item: model.SaleItems.SaleItems, file: Annotated[bytes, File()]):
    return item, file
