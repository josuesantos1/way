from fastapi import FastAPI
from pydantic import BaseModel
from ..contracts.model.quote import Quote

app = FastAPI()

@app.get("/")
def home():
    return {"say": "Hello, world"}

@app.get("/account")
def account():
    return {"account":
            {"name": "josue Santos",
             "branch": "009273-1"}}