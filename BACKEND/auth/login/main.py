from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from routes.protected import router as protected_router  # Import protected routes
from database import Base

# create_all is not used here because we have multiple engines
# Base.metadata.create_all(bind=default_engine)
# Base.metadata.create_all(bind=doctor_engine)

# Create the application
app = FastAPI(
    title="Login Microservice",
    description="A standalone backend for user authentication",
    version="1.0.0"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to a list of specific domains if necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint to check service status
@app.get("/")
def root():
    return JSONResponse({"message": "Login microservice is running successfully."})

# Include authentication routes and protected routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(protected_router, prefix="/protected", tags=["Protected"])

# Print all registered routes (for debugging)
for route in app.routes:
    if hasattr(route, "methods"):
        print(f"Route: {route.path} | Methods: {route.methods}")
    else:
        print(f"Route: {route.path} (No HTTP methods, probably a Mount)")
