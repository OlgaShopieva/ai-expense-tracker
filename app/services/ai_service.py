import requests
from app.config import AI_API_KEY

def get_advice(summary: dict) -> dict:
    prompt = f"""
    Income: {summary['income']}
    Expenses: {summary['expenses']}
    Balance: {summary['balance']}

    Give short financial advice.
    """

    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {AI_API_KEY}"},
        json={
            "model": "gpt-4.1-mini",
            "input": prompt
        }
    )

    data = response.json()

    try:
        return data["output"][0]["content"][0]["text"]
    except (KeyError, IndexError):
        print("Unexpected response:", data)
        return "Error generating advice"