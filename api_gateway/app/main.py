from fastapi import FastAPI
from app.routers import gateway

app = FastAPI(title="API Gateway")

# Incluir el router que manejará el enrutamiento hacia los microservicios
app.include_router(gateway.router)

@app.get("/")
async def root():
    return {"message": "API Gateway is running"}
