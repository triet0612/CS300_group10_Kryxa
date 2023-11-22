from io import BytesIO
from fastapi.responses import StreamingResponse
from fastapi import APIRouter, HTTPException, Response, Depends, File
from typing import Annotated
from auth import checkAdminAccount, generate_admin_token, validateAdminToken, AccountDTO

import model.PC
from model.PC import Pc, fetch_pc_by_id, insert_pc, PcDTO

import model.SaleItems
from model.SaleItems import SaleItems, create_item

import model.Bill
from model.Bill import Bill, fetch_all_bills

from model.Admin import Admin
from service.file import get_file

adminRouter = APIRouter(tags=["admin"])
file_manager = get_file()


# @adminRouter.get("/")
# async def home_admin(acc: Annotated[AccountDTO, Depends(validateAdminToken)]):
#     return {"message": "welcome admin ID: " + str(acc.ID)}


@adminRouter.post("/login")
async def login(acc: Admin, res: Response) -> str:
    try:
        valid = checkAdminAccount(acc)
        if valid is False:
            raise HTTPException(status_code=401, detail="Wrong password or id")
        res.headers.append("Authorization", generate_admin_token(acc))
        return "Login successful"
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail="Error validating")


@adminRouter.get("/bills", dependencies=[Depends(validateAdminToken)])
async def get_all_bills(Datetime: str | None = None):
    try:
        bill_list = model.Bill.fetch_all_bills()
        if len(bill_list) == 0:
            raise HTTPException(status_code=404,
                                detail="No items")  # This should not be 404, should have a notification screen

        # if Datetime:
        #     item_list[:] = [item for item in item_list if item.Category == item_category]
        return bill_list
    except HTTPException:
        pass  # ignore HTTPException


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
        raise HTTPException(status_code=404, detail="Error not found")
    except FileNotFoundError as err:
        print(err)
        raise HTTPException(status_code=404, detail='File not found')


# create item and image file
# @adminRouter.post("/get_items", dependencies=[Depends(validateAdminToken)])
# async def create_item(item: model.SaleItems.SaleItems, file: Annotated[bytes, File()]):
#     return item, file


@adminRouter.get("/pc/{pc_id}", dependencies=[Depends(validateAdminToken)])
async def fetch_pc_id(pc_id: int) -> Pc:
    try:
        pc_info = fetch_pc_by_id(pc_id)
        return pc_info
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail="No pc with that id")


@adminRouter.get("/pc", dependencies=[Depends(validateAdminToken)])
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


# @adminRouter.post("/pc/{pc_id}", dependencies=[Depends(validateAdminToken)])
# async def edit_pc(pc_info: PcDTO):
#     try:
#         return update_pc_by_id(pc_info)
#     except Exception as err:
#         print(err)
#         raise HTTPException(status_code=404, detail="PC not found")

@adminRouter.post("/item", dependencies=[Depends(validateAdminToken)], )
async def create_item(item: SaleItems):
    try:
        model.SaleItems.create_item(item)
        return item
    except AssertionError as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error create Item")


# post image
@adminRouter.post("/uploadfile/")
async def create_upload_file(file: Annotated[bytes, File()], item_id: int):
    try:
        file_manager.create_image(str(item_id), file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@adminRouter.get("/getfile/{filename}")
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
