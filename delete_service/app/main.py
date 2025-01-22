from fastapi import FastAPI
from app.routers import delete

app = FastAPI(title="Delete Appointment Service")

# Incluir el router para manejar la eliminación de citas
app.include_router(delete.router)

@app.get("/")
async def root():
    return {"message": "Delete Appointment Service is running"}
