from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.create import router as create_router

app = FastAPI()

# 🔹 Endpoint raíz para verificar que el servicio está corriendo
@app.get("/")
async def root():
    return JSONResponse(content={"message": "Appointment creation microservice working correctly"})

# 🔹 Registrar el router de creación de citas
app.include_router(create_router, prefix="/api/v1")
