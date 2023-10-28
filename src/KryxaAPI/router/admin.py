from fastapi import APIRouter, HTTPException, Response, Depends
from typing import Annotated
from auth import checkAdminAccount, generate_token, validateAdminToken, AccountDTO

adminRouter = APIRouter(tags=["admin"])

fake_items_db = [
    {
        "ItemID": "1",
        "Name": "Com ga",
        "Price": "50000",
        "Category": "Food",
        "ItemStatus": "On sale",
        "Stock": "1"
    },
    {
        "ItemID": "2",
        "Name": "Com khong ga",
        "Price": "50000",
        "Category": "Food",
        "ItemStatus": "On sale",
        "Stock": "1"
    }, {
        "ItemID": "3",
        "Name": "Com ga khong",
        "Price": "50000",
        "Category": "Food",
        "ItemStatus": "On sale",
        "Stock": "1"
    }, {
        "ItemID": "4",
        "Name": "Pepsi Lon 500ml",
        "Price": "9000",
        "Category": "Drink",
        "ItemStatus": "On sale",
        "Stock": "1"
    }, {
        "ItemID": "5",
        "Name": "Revive 500ml",
        "Price": "10000",
        "Category": "Drink",
        "ItemStatus": "On sale",
        "Stock": "1"
    }
]


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


# TODO: getAllItem()
@adminRouter.get("/items")
async def get_all_items():
    try:
        # TODO: replace fake_items_db with itemList
        # itemList = List of items get from getAllItem()
        if len(fake_items_db) == 0:
            raise HTTPException(status_code=404,
                                detail="No items")  # This should not be 404, should have a notification screen
        return fake_items_db
    except Exception as err:
        print(err)


# TODO: getItemByID(ID: int)

# TODO: getItemsByCategory(category: str)

# TODO: getItemsByName(nameString: str)
