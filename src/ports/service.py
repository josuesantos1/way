from fastapi import FastAPI
from pydantic import BaseModel
from ..contracts.model.quote import Quote

app = FastAPI()

@app.get("/")
def home():
    return {"say": "Hello, world"}

@app.get("/deliveries")
def deliveries():
    return [{"id": 1,
             "status": "done",
             "price": 10000},
            {"id": 2,
             "status": "done",
             "price": 14300},
            {"id": 3,
             "status": "done",
             "price": 5000}] 

@app.post("/deliveries/quote")
def delivery_quote(quote: Quote):
    return {"quote": ((quote.size1 + quote.size2 + quote.size3) / 3 + quote.weight) / 5,
            "time": 15}
