💰 Finance Manager – Plaid Integration
📌 About the project

Finance Manager is a lightweight web app built with Python (Flask) that integrates with the Plaid API (Sandbox).
It allows you to connect bank accounts, fetch balances and transactions, and safely store access tokens locally.

This project was created as part of an API integration exercise and is a great foundation for future fintech applications.

🚀 Features

🔑 Exchange public_token → access_token

🏦 Fetch user’s bank accounts (Plaid Sandbox)

📊 Get transactions (last 30 days)

💾 Save tokens in SQLite and JSON for persistence

🌐 Simple frontend (HTML + CSS) to test everything without Postman

🛠️ Tech Stack

Backend: Python 3.13, Flask

Database: SQLite

Storage: JSON

API: Plaid (Sandbox)

Frontend: HTML + CSS (JS/Bootstrap planned in future phase)

⚡ Quickstart
1. Clone the repo
git clone <repo_url>
cd projekt_managerfinansowy

2. Create & activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure Plaid keys

Create a .env file:

PLAID_CLIENT_ID=your_client_id
PLAID_SECRET=your_secret
PLAID_ENV=sandbox

5. Run the app
flask --app app run


Open http://127.0.0.1:5000
 in your browser 🎉 and login by user and 1234

📡 API Endpoints
Endpoint	Method	Description
/api/item/public_token/exchange	POST	Exchange public_token for access_token, save to DB & JSON
/api/accounts	GET	Fetch user accounts
/api/transactions	GET	Fetch last 30 days of transactions
/api/token	GET	View saved tokens (SQLite & JSON)
📂 Project Structure
projekt_managerfinansowy/
│
├─ app.py                  # Flask app (routes & API logic)
├─ database.py             # SQLite operations
├─ storage.py              # JSON operations
├─ services/
│   └─ plaid_client.py     # Plaid API client config
├─ tokens.json             # Local token storage
├─ tokens.db               # SQLite DB
├─ static/                 # CSS / frontend assets
└─ templates/              # HTML frontend

🔍 Usage Flow

Generate Sandbox public_token in Plaid

Exchange it via /api/item/public_token/exchange

Token gets stored in SQLite + JSON

Test other endpoints (/api/accounts, /api/transactions)

View saved tokens at /api/token

📝 Notes

Plaid Sandbox only simulates transactions from the last 30 days

Dates are saved in UTC+2

Frontend is kept minimal for testing purposes – styling/JS to be added later