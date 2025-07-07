from fastapi import FastAPI
from pydantic import BaseModel
from . import routers

class RootResponse(BaseModel):
    message: str

app = FastAPI()
app.include_router(routers.router)

@app.get("/", response_model=RootResponse) 
def read_root() -> RootResponse: 
    return RootResponse(message="Hello World") 