"""APLIKACJA FLASK"""
import os  # do obsługi zmiennych środowiskowych
from flask import Flask, request, jsonify  # Flask: framework do tworzenia API
import sqlite3

# Import klienta Plaid
from services.plaid_client import get_plaid_client

# Import modeli zapytań z Plaid SDK
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest

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
    # Pobranie identyfikatora użytkownika z parametru URL
    user_id = request.args.get("user_id")

    # Pobranie public_token z ciała żądania
    public_token = request.json["public_token"]

    # Utworzenie zapytania do Plaid
    exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
    exchange_response = plaid_client.item_public_token_exchange(exchange_request).to_dict()

    # Wyciągnięcie access_token i item_id z odpowiedzi
    access_token = exchange_response["access_token"]
    item_id = exchange_response["item_id"]

    # Zapis tokenów do bazy SQLite i pliku JSON
    save_user_token(user_id, access_token, item_id) # SQLite
    save_token_to_json(user_id, access_token, item_id) # JSON

    # Zwrócenie odpowiedzi
    return jsonify({"status": "ok", "item_id": item_id})

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

    transactions_request = TransactionsGetRequest(
        access_token=token_data["access_token"],
        start_date="2024-01-01",
        end_date="2025-12-31",
        options={"count": 10, "offset": 0}
    )
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