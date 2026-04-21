import pandas as pd

def calculate_summary(df: pd.DataFrame) -> dict:
    income = df.query("amount > 0")["amount"].sum()
    expenses = df.query("amount < 0")["amount"].sum()

    return {
        "income": float(income),
        "expenses": float(expenses),
        "balance": float(income + expenses)
    }