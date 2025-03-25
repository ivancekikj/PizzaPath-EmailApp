from fastapi import FastAPI

from app.config import load_settings
from app.middleware import RestrictBackendMiddleware
from app.routes import router

load_settings()

app = FastAPI(title="Pizza Path - Email App")

# Register Middleware
app.add_middleware(RestrictBackendMiddleware)

# Register Routes
app.include_router(router)