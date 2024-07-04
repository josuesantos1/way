from pydantic import BaseModel

class Account(BaseModel):
    name: str
    email: str
    password: str
    tax_id: str
    
class BankAccount(BaseModel):
    brach: str
    agency: str
    tax_id: str
    balance: int

