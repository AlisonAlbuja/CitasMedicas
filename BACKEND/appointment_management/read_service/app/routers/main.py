from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers.read import router as read_router

app = FastAPI(title="Read Service", description="Service for reading quotes", version="1.0.0")

# Root endpoint to check service status
@app.get("/")
def root():
    return JSONResponse({"message": "Read service is running successfully."})

# Include the reading router
app.include_router(read_router, prefix="/api/v1")
