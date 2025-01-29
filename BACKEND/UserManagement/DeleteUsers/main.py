from fastapi import FastAPI
from routes.user import user_bp

# Create an instance of the FastAPI application
app = FastAPI()

# Include the microservice routes
app.include_router(user_bp)

# Root endpoint to check if the microservice is running
@app.get("/")
def root():
    return {"message": "DeleteUsers microservice is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
