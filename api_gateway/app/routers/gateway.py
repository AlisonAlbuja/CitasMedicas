import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter()

# URLs de los microservicios
CREATE_SERVICE_URL = "http://create_service:8000"
READ_SERVICE_URL = "http://read_service:8001"
UPDATE_SERVICE_URL = "http://update_service:8002"
DELETE_SERVICE_URL = "http://delete_service:8003"

@router.post("/appointments")
async def create_appointment(payload: dict):
    """Redirige la solicitud al servicio de creación."""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{CREATE_SERVICE_URL}/appointments", json=payload)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

@router.get("/appointments")
async def get_appointments():
    """Redirige la solicitud al servicio de lectura."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{READ_SERVICE_URL}/appointments")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

@router.get("/appointments/{id}")
async def get_appointment_by_id(id: str):
    """Redirige la solicitud al servicio de lectura por ID."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{READ_SERVICE_URL}/appointments/{id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

@router.put("/appointments/{id}")
async def update_appointment(id: str, payload: dict):
    """Redirige la solicitud al servicio de actualización."""
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{UPDATE_SERVICE_URL}/appointments/{id}", json=payload)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()

@router.delete("/appointments/{id}")
async def delete_appointment(id: str):
    """Redirige la solicitud al servicio de eliminación."""
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{DELETE_SERVICE_URL}/appointments/{id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.json())
        return response.json()
