from fastapi import FastAPI
from app.routers import read

app = FastAPI(title="Read Appointment Service")

# Registrar el router
app.include_router(read.router)

@app.get("/")
async def root():
    return {"message": "Read Appointment Service is running"}
