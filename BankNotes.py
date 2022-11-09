from pydantic import BaseModel

class BankNote(BaseModel):
    Income : float
    Age: float
    Experience : float
    Married_Single :int
    Car_Ownership : int
    CURRENT_JOB_YRS : float
    CURRENT_HOUSE_YRS :float