from fastapi import FastAPI
from pydantic import BaseModel
from . import routers
from . import models

class RootResponse(BaseModel):
    message: str

app = FastAPI()
app.include_router(routers.router)

models.create_db_and_tables()

@app.get("/", response_model=RootResponse) 
def read_root() -> RootResponse: 
    return RootResponse(message="Hello World") 