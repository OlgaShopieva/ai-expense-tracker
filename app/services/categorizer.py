CATEGORIES = {
    "coffee": "Food",
    "groceries": "Food",
    "uber": "Transport",
    "salary": "Income",
}

def categorize(description: str) -> str:
    description = description.lower()

    return next(
        (value for key, value in CATEGORIES.items() if key in description),
        "Other"
    )