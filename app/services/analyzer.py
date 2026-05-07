import pandas as pd
from app.models.transaction import Transaction
from typing import List

def calculate_summary(transactions: List[Transaction]) -> dict:
    income = sum(t.amount for t in transactions if t.amount > 0)
    expenses = sum(t.amount for t in transactions if t.amount < 0)

    return {
        "income": float(income),
        "expenses": float(expenses),
        "balance": float(income + expenses)
    } 