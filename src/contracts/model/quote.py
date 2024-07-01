from pydantic import BaseModel


class Quote(BaseModel):
    weight: int
    size1: int
    size2: int
    size3: int
    start_cep: str
    end_cep: str
    