from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.create import router as create_router

app = FastAPI()

# 🔹 Root endpoint to verify that the service is running
@app.get("/")
async def root():
    return JSONResponse(content={"message": "Appointment creation microservice working correctly"})

# 🔹 Registrar el router de creación de citas
app.include_router(create_router, prefix="/api/v1")
