from fastapi import FastAPI
from app.routers.delete import router as delete_router

app = FastAPI()

# 📌 Endpoint raíz para verificar si el microservicio está activo
@app.get("/")
def root():
    return {"message": "Delete Service is running 🚀"}

# 📌 Incluir las rutas de eliminación
app.include_router(delete_router, prefix="/api/v1")
