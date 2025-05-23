from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World from Azure !"}

@app.get("/health")
def health_status():
    return {"up": True}

@app.get("/ready")
def readiness_status():
    return {"ready": True}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}