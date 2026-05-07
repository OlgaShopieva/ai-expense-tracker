from fastapi import FastAPI
import pandas as pd
from app.models.transaction import Transaction

from app.services.analyzer import calculate_summary
from app.services.categorizer import categorize
from app.services.ai_service import get_advice
from app.config import DATA_PATH

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/summary")
def get_summary():
    df = pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'])

    transactions = []
    for _, row in df.iterrows():
        transaction = Transaction(
            date=row['date'],
            amount=row['amount'],
            description=row['description'],
            category=None
        )
        transactions.append(transaction)
    
    for t in transactions:
        t.category = categorize(t.description)

    summary = calculate_summary(transactions)

    print(summary)

    advice = get_advice(summary)

    return advice