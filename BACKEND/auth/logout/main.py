from fastapi import FastAPI
from routes import logout

app = FastAPI(title="Microservicio de Logout")

# Incluir las rutas
app.include_router(logout.router)

@app.get("/")
def home():
    return {"message": "Microservicio de Logout activo"}
