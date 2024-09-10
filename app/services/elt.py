import pandas as pd
from fastapi import UploadFile, HTTPException
import io


class ETL:

    def __init__(self):
        pass

    def extract_data_from_csv(self, file: UploadFile) -> pd.DataFrame:

        try:
            data_bytes = file.file.read()
            data_string = data_bytes.decode('latin-1')
            df = pd.read_csv(io.StringIO(data_string))
            print(df.head(5))
            return df
        except Exception as exception:
            print(exception)
            raise HTTPException(status_code=501, detail='error extracting file content')
        
    def mapping_data_to_database(self):
        pass
