from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.protected import router as protected_router  # Importar rutas protegidas
from database import Base

# No se usa create_all aquí porque tenemos múltiples motores
# Base.metadata.create_all(bind=default_engine)
# Base.metadata.create_all(bind=doctor_engine)

# Crear la aplicación
app = FastAPI(
    title="Login Microservice",
    description="A standalone backend for user authentication",
    version="1.0.0"
)

# Configurar CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar "*" por una lista de dominios específicos si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint raíz para verificar el estado del servicio
@app.get("/")
def root():
    return JSONResponse({"message": "Login microservice is running successfully."})

# Incluir rutas de autenticación y rutas protegidas
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(protected_router, prefix="/protected", tags=["Protected"])

# Imprimir todas las rutas registradas (para debugging)
for route in app.routes:
    if hasattr(route, "methods"):
        print(f"Route: {route.path} | Methods: {route.methods}")
    else:
        print(f"Route: {route.path} (No HTTP methods, probably a Mount)")
