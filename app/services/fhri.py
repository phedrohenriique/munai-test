import asyncio
from fhirpy import AsyncFHIRClient


class FhirPy():
    
    def __init__(self) -> None:
        pass

    def create_client(self):
        # Create an instance
        client = AsyncFHIRClient(
            'http://fhir-server/',
            authorization='Bearer TOKEN',
        )
        return client

# Fast Healthcare Interoperability Resource main class


class FHRI(
    FhirPy
):

    def __init__(self) -> None:
        pass
