import uvicorn
import routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     job.adding_scheduler()
#     yield
#     print("server off")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(routes.router_server)
app.include_router(routes.router_patients)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8800,
        reload=True,
        log_level="debug",
        workers=2
    )
