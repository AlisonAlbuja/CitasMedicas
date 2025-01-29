from fastapi import FastAPI
from routes import user
import uvicorn

app = FastAPI()

# Register the routes of the microservice
app.include_router(user.router)

# Root route to test if the service is working
@app.get("/")
def read_root():
    return {"message": "User Visualization Service is working"}

# Main entry point
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9100, reload=True)
