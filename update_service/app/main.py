from fastapi import FastAPI
from app.routers import update

app = FastAPI(title="Update Appointment Service")

# Incluir el router para manejar la actualización de citas
app.include_router(update.router)

@app.get("/")
async def root():
    return {"message": "Update Appointment Service is running"}
