from fastapi import FastAPI
from app.routers.delete import router as delete_router

app = FastAPI()

app.include_router(delete_router, prefix="/api/v1")
