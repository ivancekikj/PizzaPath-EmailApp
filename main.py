from fastapi import FastAPI

from app.config import load_settings
from app.routes import router

load_settings()

app = FastAPI(title="Pizza Path - Email App")

# Register Routes
app.include_router(router)