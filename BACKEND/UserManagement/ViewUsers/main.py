from fastapi import FastAPI
from routes import user
import uvicorn

app = FastAPI()

# Registrar las rutas del microservicio
app.include_router(user.router)

# Ruta raíz para probar si el servicio está funcionando
@app.get("/")
def read_root():
    return {"message": "Servicio Visualizar Usuarios funcionando"}

# Punto de entrada principal
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9100, reload=True)
