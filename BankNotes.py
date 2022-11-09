from pydantic import BaseModel

class BankNote(BaseModel):
    Income : int
    Age: int
    Experience : int
    Married_Single :int
    Car_Ownership : int
    CURRENT_JOB_YRS : int
    CURRENT_HOUSE_YRS :int