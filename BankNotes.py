from pydantic import BaseModel

class BankNote(BaseModel):
    balance: float
    AnnualSalary: float
    Employed : int