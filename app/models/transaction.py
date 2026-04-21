from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    date: datetime
    amount: float
    description: str
    category: str | None = None