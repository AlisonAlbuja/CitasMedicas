from fastapi import FastAPI
from routes.user import user_bp

# 📌 Crear una instancia de la aplicación FastAPI
app = FastAPI(title="DeleteUsers Microservice", version="1.0")

# 📌 Incluir rutas con un prefijo
app.include_router(user_bp, prefix="/users", tags=["Users"])

# 📌 Ruta principal para verificar el estado del microservicio
@app.get("/")
def root():
    return {"message": "DeleteUsers microservice is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
