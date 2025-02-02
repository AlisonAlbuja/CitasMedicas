from fastapi import FastAPI
from routes.user import user_bp

# Crear instancia de la aplicación FastAPI
app = FastAPI()

# Incluir las rutas del microservicio
app.include_router(user_bp)

# Endpoint raíz para verificar que el microservicio esté funcionando
@app.get("/")
def root():
    return {"message": "DeleteUsers microservice is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)