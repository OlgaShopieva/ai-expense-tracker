from fastapi import Depends, FastAPI, HTTPException
import pandas as pd
from sqlalchemy.orm import Session

from app.services.analyzer import calculate_summary
from app.services.categorizer import categorize
from app.services.ai_service import get_advice
from app.models.transaction import Transaction, TransactionDB
from app.config import DATA_PATH
from app.db import SessionLocal, get_db, init_db

app = FastAPI()

def load_initial_transactions() -> None:
    with SessionLocal() as db:
        if db.query(TransactionDB).count() == 0:
            df = pd.read_csv(DATA_PATH)
            df["date"] = pd.to_datetime(df["date"])

            for row in df.itertuples(index=False):
                db.add(
                    TransactionDB(
                        date=row.date,
                        amount=row.amount,
                        description=row.description,
                        category=categorize(row.description),
                    )
                )

            db.commit()


@app.on_event("startup")
def startup_event():
    init_db()
    load_initial_transactions()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/transactions", response_model=list[Transaction])
def list_transactions(db: Session = Depends(get_db)):
    return db.query(TransactionDB).all()

@app.post("/transactions", response_model=Transaction, status_code=201)
def create_transaction(transaction: Transaction, db: Session = Depends(get_db)):
    db_transaction = TransactionDB(
        date=transaction.date,
        amount=transaction.amount,
        description=transaction.description,
        category=transaction.category or categorize(transaction.description),
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    transactions = db.query(TransactionDB).all()
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found")

    summary = calculate_summary(transactions)
    advice = get_advice(summary)

    return {"summary": summary, "advice": advice}