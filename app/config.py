import os
from dotenv import load_dotenv

load_dotenv()

AI_API_KEY = os.getenv("AI_API_KEY")
DATA_PATH = "data/transactions.csv"
DATABASE_URL = os.getenv("DATABASE_URL")