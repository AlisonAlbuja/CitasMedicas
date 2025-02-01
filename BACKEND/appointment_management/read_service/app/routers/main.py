from fastapi import FastAPI
from app.routers.read import router as read_router

app = FastAPI()

app.include_router(read_router, prefix="/api/v1")
