from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException


class PageServer(StaticFiles):
    async def get_response(self, path: str, scope):
        try:
            return await super().get_response(path, scope)
        except (HTTPException, StarletteHTTPException) as err:
            if err.status_code == 404:
                return await super().get_response('index.html', scope)
            else:
                raise err
