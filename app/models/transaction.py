from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TransactionDB(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=True)


class Transaction(BaseModel):
    id: int | None = None
    date: datetime
    amount: float
    description: str
    category: str | None = None

    class Config:
        from_attributes = True
