from fastapi import FastAPI
from . import routers

app = FastAPI()
app.include_router(routers.router)

# Print docs URL on startup
@app.on_event("startup")
async def show_docs_url():
    print("\nYour FastAPI docs are available at: http://127.0.0.1:8000/docs\n")


@app.get("/")
def read_root() -> dict:
    return {"Hello": "World"}