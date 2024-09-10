from fastapi import APIRouter, FastAPI

app = FastAPI()
router_server = APIRouter()


@router_server.get("/server")
async def get_server_status():
    server_response = {"message": "sever on"}
    return server_response
