import uvicorn
from fastapi import FastAPI
from router.admin import adminRouter


def get_server():
    app_router = FastAPI()
    app_router.include_router(adminRouter, prefix="/admin")
    return app_router


if __name__ == '__main__':
    server = get_server()
    uvicorn.run(server, host='localhost', port=8000)
