from fastapi import APIRouter

adminRouter = APIRouter(tags=["admin"])


@adminRouter.get("/")
async def home_admin():
    return {
        "message": "this is home admin"
    }
