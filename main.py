
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world_root():
    return {"Hello": "World"}
