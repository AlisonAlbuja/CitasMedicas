from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.read import router as read_router

app = FastAPI(title="Read Service", description="Servicio para leer citas", version="1.0.0")

# Endpoint raíz para verificar el estado del servicio
@app.get("/")
def root():
    return JSONResponse({"message": "Read service is running successfully."})

# Incluir el router de lectura
app.include_router(read_router, prefix="/api/v1")
