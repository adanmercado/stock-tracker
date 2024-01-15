from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from api.config import Session

class DatabaseSessionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            request.state.db = Session()
            return await call_next(request)
        except Exception as e:
            print(e)
            return JSONResponse(status_code=500, content={
                'error': str(e)
            })
        finally:
            request.state.db.close()