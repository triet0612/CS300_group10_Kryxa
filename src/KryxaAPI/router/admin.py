import sqlite3
import datetime
from datetime import datetime
from io import BytesIO
from fastapi.responses import StreamingResponse
from fastapi import APIRouter, HTTPException, Response, Depends, File
from typing import Annotated

from model.PC import Pc, start_session, terminate_session
from fastapi import APIRouter, HTTPException, Response, Depends, File, Query
from fastapi.responses import StreamingResponse

import model.Bill
import model.PC
from service.auth import checkAdminAccount, generate_admin_token, validateAdminToken, AccountDTO, change_password
import model.SaleItems

from model.Admin import Admin
from model.Bill import fetchSalesByMonth, fetchSalesByPcID
from model.PC import Pc, fetch_pc_by_id, insert_pc, PcDTO, fetch_time_usage, update_pc_by_id
from model.SaleItems import SaleItems
from service.file import get_file
from model.Bill import Bill, fetch_bill_byID
from model.Bill import fetchSalesByMonth, fetchSalesByPcID, checkBillRequireConfirm
from model.FoodQueue import get_food_queue, insert_to_food_queue, FoodItem, delete_food

adminRouter = APIRouter(tags=["admin"])
file_manager = get_file()


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


@adminRouter.get("/bills/", dependencies=[Depends(validateAdminToken)])
async def get_all_bills(
        bill_id: Annotated[int, Query(ge=1)] = None,
        day: Annotated[int, Query(ge=1, le=31)] = None,
        month: Annotated[int, Query(ge=1, le=12)] = None,
        year: Annotated[int, Query(ge=0)] = None, ):
    try:
        bill_list = model.Bill.fetch_all_bills()
        if len(bill_list) == 0:
            raise HTTPException(status_code=404, detail="No items")
        if day and month and year:
            time_obj = datetime.strptime(f'{year}-{month}-{day}', "%Y-%m-%d")
            bill_list[:] = [bill for bill in bill_list if time_obj.date() == bill.Datetime.date()]
        if bill_id:
            bill_list[:] = [bill for bill in bill_list if bill.BillID == bill_id]
        return bill_list
    except HTTPException:
        pass


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


# update item
@adminRouter.put("/items/{item_id}", dependencies=[Depends(validateAdminToken)])
async def update_item(new_item_data: SaleItems):
    try:
        t = model.SaleItems.update_item(new_item_data)
        print(t)
    # except FileNotFoundError as err:
    #     print(err)
    except Exception as err:
        print(err)


# delete item
@adminRouter.delete("/items/{item_id}", dependencies=[Depends(validateAdminToken)], )
async def delete_item(item_id: int):
    try:
        model.SaleItems.delete_item(item_id)
    except Exception as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error delete Item")


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


@adminRouter.put("/pc/{pc_id}", dependencies=[Depends(validateAdminToken)])
async def edit_pc(pc_info: PcDTO):
    try:
        return update_pc_by_id(pc_info)
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail="PC not found")


@adminRouter.post("/item", dependencies=[Depends(validateAdminToken)])
async def create_item(item: SaleItems):
    try:
        model.SaleItems.create_item(item)
        return item
    except sqlite3.Error as err:
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


@adminRouter.post("/account")
async def check_password(acc: Admin) -> str:
    try:
        valid = checkAdminAccount(acc)
        if valid is False:
            raise HTTPException(status_code=401, detail="Wrong password ")
        return "Check password successful"
    except Exception as err:
        print(err)
        raise HTTPException(status_code=401, detail="Error validating")


@adminRouter.put("/account")
async def get_new_password(acc: Admin):
    try:
        return change_password(acc)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error saving password")


@adminRouter.post("/session", dependencies=[Depends(validateAdminToken)])
async def session(PcID: int | None = None, time: int | None = None):
    if PcID is not None and time is not None:
        try:
            start_session(PcID, time)
        except HTTPException as err:
            raise err
        except sqlite3.Error as err:
            print(err)
            raise HTTPException(status_code=400, detail="Error open a session")
        except Exception as err:
            print(err)
            raise HTTPException(status_code=500, detail="Unknown error")
    elif PcID is not None:
        try:
            terminate_session(PcID)
        except HTTPException as err:
            raise err
        except sqlite3.Error as err:
            print(err)
            raise HTTPException(status_code=400, detail="Error termination session")
        except Exception as err:
            print(err)
            raise HTTPException(status_code=500, detail="Unknown error")


@adminRouter.get("/sales", dependencies=[Depends(validateAdminToken)])
async def get_sale(
        month: Annotated[int | None, Query(ge=1, le=12)] = None,
        year: Annotated[int | None, Query(ge=0)] = None
):
    if month is not None and year is not None:
        try:
            res = fetchSalesByMonth(month, year)
            return res
        except HTTPException as err:
            raise err
        except Exception as err:
            print(err)
            raise HTTPException(500, "Unknown error")
    else:
        try:
            res = fetchSalesByPcID()
            return res
        except HTTPException as err:
            raise err
        except Exception as err:
            print(err)
            raise HTTPException(500, "Unknown error")


@adminRouter.get("/pc/time/", dependencies=[Depends(validateAdminToken)])
def get_time_usage():
    try:
        res = fetch_time_usage()
        return res
    except HTTPException as err:
        print(err)
        raise err
    except Exception as err:
        print(err)
        raise HTTPException(500, "Unknown error")


@adminRouter.get("/bills/{bill_id}", dependencies=[Depends(validateAdminToken)])
async def view_bill_info(bill_id: int) -> Bill:
    try:
        bill_info = fetch_bill_byID(bill_id)
        return bill_info
    except Exception as err:
        print(err)
        raise HTTPException(status_code=404, detail="No bill with that id")


@adminRouter.put("/bills/{bill_id}", dependencies=[Depends(validateAdminToken)])
async def update_bill(new_bill_data: Bill):
    try:
        bill_info = model.Bill.update_bill(new_bill_data)
        print(bill_info)
    # except FileNotFoundError as err:
    #     print(err)
    except Exception as err:
        print(err)


@adminRouter.post("/open/", dependencies=[Depends(validateAdminToken)])
async def open_session(PcID: int, time: int):
    try:
        start_session(PcID, time)
    except HTTPException as err:
        raise err
    except sqlite3.Error as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error open a session")
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Unknown error")


@adminRouter.get("/bill_notif")
async def bill_notif():
    try:
        ans = checkBillRequireConfirm()
        return {"Message": str(ans)}
    except HTTPException as err:
        raise err
    except sqlite3.Error as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error checking")
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Unknown error")


@adminRouter.get("/food_queue")
async def fetch_food_queue():
    try:
        ans = get_food_queue()
        return ans
    except HTTPException as err:
        raise err
    except sqlite3.Error as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error get food_queue")
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Unknown error")


@adminRouter.post("/delete_food_queue")
def delete_food_queue(food: FoodItem):
    try:
        print(food)
        delete_food(food)
    except HTTPException as err:
        raise err
    except sqlite3.Error as err:
        print(err)
        raise HTTPException(status_code=400, detail="Error get food_queue")
    except Exception as err:
        print(err)
        raise HTTPException(status_code=500, detail="Unknown error")
