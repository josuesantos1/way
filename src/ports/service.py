from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"say": "Hello, world"}

class Quote(BaseModel):
    weight: int
    size1: int
    size2: int
    size3: int
    start_cep: str
    end_cep: str

@app.post("/deliveries/quote")
def delivery_quote(quote: Quote):
    return {"quote": ((quote.size1 + quote.size2 + quote.size3) / 3 + quote.weight) / 5,
            "time": 15}

