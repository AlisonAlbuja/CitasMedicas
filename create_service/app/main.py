from fastapi import FastAPI
from app.routers import create

# Crea la instancia de FastAPI
app = FastAPI(title="Create Appointment Microservice")

# Incluye los routers para los endpoints de la API
app.include_router(create.router)

# Endpoint raíz para verificar que el servicio está funcionando
@app.get("/")
async def root():
    return {"message": "Create Appointment Service is running"}
