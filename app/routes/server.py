from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.get("/server")
async def get_server_status():
    server_response = {"message": "sever on"}
    return server_response
