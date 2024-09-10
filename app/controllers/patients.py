from services.database import DatabaseService
from fastapi import HTTPException

database_service = DatabaseService(type="sqlalchemy").create()

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
       