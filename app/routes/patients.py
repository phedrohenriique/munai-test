from fastapi import APIRouter, FastAPI, UploadFile
from controllers import patients

app = FastAPI()
router_patients = APIRouter()

@router_patients.get("/patients")
async def get_patients_list():
    server_response = await patients.get_patients_list()
    return server_response


@router_patients.post("/patients/file")
async def post_patients_file(file: UploadFile):
    server_response = await patients.extract_data_from_csv(file)
    return server_response
