from pydantic import BaseModel

class Transaction(BaseModel):
    id: str
    type: str
    transaction_at: str
    status: str
    account: str
    


