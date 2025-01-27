from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from database import Base, engine

# Inicializar la base de datos
Base.metadata.create_all(bind=engine)

# Crear la app
app = FastAPI(
    title="Login Microservice",
    description="A standalone backend for user authentication",
    version="1.0.0"
)

# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por una lista específica de dominios si lo necesitas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz para verificar el estado del servicio
@app.get("/")
def root():
    return JSONResponse({"message": "Login microservice is running successfully."})

# Incluir las rutas del servicio de autenticación
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# Imprimir todas las rutas registradas para depuración
for route in app.routes:
    if hasattr(route, "methods"):  # Verifica si el objeto tiene el atributo 'methods'
        print(f"Route: {route.path} | Methods: {route.methods}")
    else:
        print(f"Route: {route.path} (No HTTP methods, probablemente un Mount)")
