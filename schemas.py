#creating the schema for the endpoint 

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


#design the schema for the create_expense endpoint
class ExpenseRequest(BaseModel):
    id:int
    date: Optional[datetime]=None
    description: str
    currency: str
    amount: float
    
class config:
    orm_mode = True


