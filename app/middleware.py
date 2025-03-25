from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.config import ADMIN_APP


class RestrictBackendMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_origin = request.headers.get("host", "")
        if request_origin != ADMIN_APP:
            raise HTTPException(status_code=403, detail="Unauthorized backend service")
        return await call_next(request)