💰 AI Expense Tracker

A Python-based API service for analyzing personal expenses, categorizing transactions, and generating AI-powered financial insights.

🚀 Features
📊 Transaction analysis using pandas
🏷️ Automatic expense categorization
🤖 AI-generated financial advice
⚡ Fast REST API built with FastAPI
📈 Ready for extension (ML, DB, dashboards)
🧠 Tech Stack
Python 3.11+
FastAPI
Pandas / NumPy
Requests (API integration)
Pydantic (data validation)
Uvicorn (ASGI server)


⚙️ Setup
1. Clone the repository
git clone https://github.com/your-username/ai-expense-tracker.git
cd ai-expense-tracker

2. Create virtual environment
python -m venv venv

Activate it:

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set environment variables

Create a .env file:
API_KEY=your_api_key_here

▶️ Run the project
python -m uvicorn app.main:app --reload

🤖 AI Integration
The app integrates with an AI API to generate financial advice based on user spending patterns.