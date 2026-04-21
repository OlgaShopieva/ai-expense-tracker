from fastapi import FastAPI
import pandas as pd

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

    df["category"] = [
        categorize(desc) for desc in df["description"]
    ]

    summary = calculate_summary(df)

    print(summary)

    advice = get_advice(summary)

    return advice