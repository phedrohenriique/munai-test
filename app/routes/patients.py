from fastapi import APIRouter, FastAPI
from controllers.patients import get_patients_list

app = FastAPI()
router = APIRouter()


@router.get("/patients")
async def get_server_status():
    server_response =  await get_patients_list()
    return server_response
    
        