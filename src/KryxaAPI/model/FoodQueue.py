from pydantic import BaseModel, Field
from typing import Annotated

from db.database import DBService


class FoodItem(BaseModel):
    PcID: Annotated[int, Field(ge=0)]
    ItemID: Annotated[int, Field(ge=1)]
    Qt: Annotated[int, Field(ge=1)]


def get_food_queue():
    food_queue = []
    with DBService() as cur:
        try:
            pc_info = cur.cursor().execute(
                "SELECT * FROM FOOD_QUEUE"
            ).fetchall()
            for i in pc_info:
                food_queue.append(FoodItem(PcID=int(i[0]), ItemID=int(i[1]), Qt=int(i[2])))
            return food_queue
        except Exception as err:
            print(err)


def insert_to_food_queue(food: FoodItem):
    with DBService() as cur:
        try:
            cur.execute(
                "INSERT INTO FOOD_QUEUE VALUES (?, ?, ?)",
                [food.PcID, food.ItemID, food.Qt]
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)


def delete_food(food: FoodItem):
    with DBService() as cur:
        try:
            cur.execute(
                'DELETE FROM "FOOD_QUEUE" WHERE ("PcID"=? AND "ItemID"=?) AND "Qt"=?',
                [food.PcID, food.ItemID, food.Qt]
            )
            cur.commit()
        except Exception as err:
            cur.rollback()
            print(err)
