from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routes.auth import router as auth_router
from database import Base, engine

# Initialize the database
Base.metadata.create_all(bind=engine)

# Create the app
app = FastAPI(
    title="Login Microservice",
    description="A standalone backend for user authentication",
    version="1.0.0"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to a specific list of domains if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint to check service status
@app.get("/")
def root():
    return JSONResponse({"message": "Login microservice is running successfully."})

# Include authentication service routes
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# Print all registered routes for debugging
for route in app.routes:
    if hasattr(route, "methods"):  # Check if the object has the 'methods' attribute
        print(f"Route: {route.path} | Methods: {route.methods}")
    else:
        print(f"Route: {route.path} (No HTTP methods, probably a Mount)")
