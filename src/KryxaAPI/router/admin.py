from fastapi import APIRouter, HTTPException, Response, Depends
from typing import Annotated
from auth import checkAdminAccount, generate_token, validateAdminToken, AccountDTO

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


fake_items_db = [
    {
        "ItemID": 1,
        "Name": "Com ga",
        "Price": 50000,
        "Category": "Food",
        "ItemStatus": "On sale",
        "Stock": 1
    },
    {
        "ItemID": 2,
        "Name": "Com khong ga",
        "Price": 50000,
        "Category": "Food",
        "ItemStatus": "On sale",
        "Stock": 1
    }, {
        "ItemID": 3,
        "Name": "Com ga khong",
        "Price": 50000,
        "Category": "Food",
        "ItemStatus": "On sale",
        "Stock": 1
    }
]

@adminRouter.get("/items/{item_id}")
async def read_item(item_id: int):
    try:
        for item in fake_items_db:
            if item_id == item["ItemID"]:
                return item
        raise HTTPException(status_code=404, detail="Item id does not exist")
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail="Item id does not exist")
