import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.admin import adminRouter
from service.page import PageServer


def get_server():
    app_router = FastAPI()

    app_router.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost', 'http://localhost:5173', 'http://localhost:8000'],
        allow_credentials=True,
        allow_methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["Authorization"]
    )

    app_router.include_router(adminRouter, prefix="/api/admin")
    app_router.mount("/", PageServer(directory="./bin/www", html=True))
    return app_router


if __name__ == '__main__':
    server = get_server()
    uvicorn.run(server, host='localhost', port=8000)
