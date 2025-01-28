from fastapi import FastAPI
from app.routers.update import router as update_router

app = FastAPI()

app.include_router(update_router, prefix="/api/v1")
