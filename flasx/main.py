from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from . import routers
from . import models

class RootResponse(BaseModel):
    message: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    # Startup
    await models.init_db()
    yield
    # Shutdown
    await models.close_db()

app = FastAPI(lifespan=lifespan)
app.include_router(routers.router)

@app.get("/", response_model=RootResponse) 
def read_root() -> RootResponse: 
    return RootResponse(message="Hello World") 