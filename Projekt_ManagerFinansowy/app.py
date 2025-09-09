"""APLIKACJA FLASK"""
import os  # do obsługi zmiennych środowiskowych
from flask import Flask, request, jsonify, render_template  # Flask: framework do tworzenia API
import sqlite3
from datetime import datetime, timedelta

# Import klienta Plaid
from services.plaid_client import get_plaid_client

# Import modeli zapytań z Plaid SDK
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.products import Products
from plaid.model.country_code import CountryCode

# Import funkcji do zapisu i odczytu tokenów
from database import initialize_database, save_user_token, get_user_token
from storage import save_token_to_json, get_token_from_json

# Utworzenie aplikacji Flask
app = Flask(__name__)

# Utworzenie klienta Plaid
plaid_client = get_plaid_client()

# Inicjalizacja bazy danych SQLite
initialize_database()

# 1 Endpoint: wymiana public_token na access_token
@app.post("/api/item/public_token/exchange")
def exchange_public_token():
    print("DEBUG: Endpoint /exchange został wywołany")
    user_id = request.args.get("user_id", "user_1")

    # 1) bezpieczne pobranie JSON
    data = request.get_json(silent=True) or {}
    public_token = data.get("public_token")
    if not public_token:
        return jsonify({
            "error": "Missing 'public_token' in JSON body",
            "hint": "Wyślij POST z Content-Type: application/json i body: {\"public_token\": \"public-sandbox-...\"}"
        }), 400

    try:
        # 2) wymiana tokenu
        req = ItemPublicTokenExchangeRequest(public_token=public_token)
        res = plaid_client.item_public_token_exchange(req).to_dict()

        access_token = res["access_token"]
        item_id = res["item_id"]

        # 3) zapis do SQLite + JSON
        save_user_token(user_id, access_token, item_id)
        save_token_to_json(user_id, access_token, item_id)

        return jsonify({
            "status": "ok",
            "user_id": user_id,
            "item_id": item_id
        })

    except ApiException as e:
        # 4) czytelny komunikat z Plaida (zamiast 500)
        try:
            details = json.loads(e.body)
        except Exception:
            details = {"raw": e.body}
        return jsonify({
            "error": "Plaid API error on exchange",
            "details": details
        }), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
# 2 Endpoint: pobierz konta użytkownika
@app.get("/api/accounts")
def get_accounts():
    user_id = request.args.get("user_id")
    token_data = get_user_token(user_id)

    if not token_data:
        return jsonify({"error": "Brak zapisanych danych dla użytkownika"}), 404

    accounts_request = AccountsGetRequest(access_token=token_data["access_token"])
    accounts_response = plaid_client.accounts_get(accounts_request).to_dict()

    return jsonify(accounts_response)

# 3 Endpoint: pobierz transakcje użytkownika
@app.get("/api/transactions")
def get_transactions():
    user_id = request.args.get("user_id")
    token_data = get_user_token(user_id)

    if not token_data:
        return jsonify({"error": "Brak zapisanych danych dla użytkownika"}), 404

    # Sandbox generuje dane tylko dla ostatnich 30 dni
    today = datetime.today().date()              # typ date
    thirty_days_ago = today - timedelta(days=7) # typ date

    transactions_request = TransactionsGetRequest(
        access_token=token_data["access_token"],
        start_date=thirty_days_ago,  # **typ date**
        end_date=today,              # **typ date**
        options={"count": 5, "offset": 0}
    )
    # Debug: sprawdzenie tokenu i dat
    print("DEBUG: Access token:", token_data["access_token"])
    print("DEBUG: Start date:", thirty_days_ago)
    print("DEBUG: End date:", today)

    transactions_response = plaid_client.transactions_get(transactions_request).to_dict()

    return jsonify(transactions_response)

# 4 Endpoint: podgląd zapisanych tokenów (SQLite i JSON)
@app.get("/api/token")
def get_stored_token():
    user_id = request.args.get("user_id")

    sqlite_token = get_user_token(user_id)
    json_token = get_token_from_json(user_id)

    return jsonify({
        "sqlite": sqlite_token,
        "json": json_token
    })

@app.post("/api/sandbox/create_item")
def sandbox_create_item():
    user_id = request.args.get("user_id")

    # 1. Tworzenie public_token w Sandboxie
    public_token_request = SandboxPublicTokenCreateRequest(
        institution_id="ins_109508",  # przykładowa instytucja sandbox
        initial_products=["transactions"]
    )
    public_token_response = plaid_client.sandbox_public_token_create(public_token_request).to_dict()
    public_token = public_token_response["public_token"]

    # 2. Wymiana public_token na access_token
    exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
    exchange_response = plaid_client.item_public_token_exchange(exchange_request).to_dict()
    access_token = exchange_response["access_token"]
    item_id = exchange_response["item_id"]

    # 3. Zapis w SQLite i JSON
    save_user_token(user_id, access_token, item_id)
    save_token_to_json(user_id, access_token, item_id)

    return jsonify({
        "status": "ok",
        "user_id": user_id,
        "access_token": access_token,
        "item_id": item_id
    })

@app.get("/api/link/token/create")
def create_link_token():
    user_id = request.args.get("user_id", "user_1")

    try:
        request_data = LinkTokenCreateRequest(
            user={"client_user_id": user_id},
            client_name="Finance Manager",
            products=[Products("transactions")],
            language="en",
            country_codes=[CountryCode("US")]
        )

        response = plaid_client.link_token_create(request_data)
        return jsonify(response.to_dict())

    except Exception as e:
        # Obsługa błędów żeby zamiast 500 pokazać info
        return jsonify({"error": str(e)}), 400

@app.get("/")
def index():
    return render_template("index.html")