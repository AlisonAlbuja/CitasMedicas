from fastapi import FastAPI
from app.routers.create import router as create_router

app = FastAPI()

app.include_router(create_router, prefix="/api/v1")

