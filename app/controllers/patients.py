from services.database import DatabaseService
from fastapi import HTTPException
from services import ETL
from fastapi import UploadFile

database_service = DatabaseService(type="sqlalchemy").create()
elt_service = ETL()

async def get_patients_list():
    try:
        result = database_service.get_patients_list()
        return result
    except Exception as exception:
        database_service.connection().rollback()
        print(exception)
        raise HTTPException(status_code=501, detail='server error')
    finally:
        database_service.connection().close()
       
async def extract_data_from_csv(file: UploadFile):
    try:
        elt_service.extract_data_from_csv(file)
        return {"message":"file upload"}
    except Exception as exception:
        print(exception)
        raise HTTPException(status_code=501, detail='file not uploaded')