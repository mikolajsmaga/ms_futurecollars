"""KLIENT PLAID"""
import os
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from plaid.api.plaid_api import PlaidApi
from dotenv import load_dotenv

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

# ✅ Sprawdzenie czy są klucze API
if not os.getenv("PLAID_CLIENT_ID") or not os.getenv("PLAID_SECRET"):
    raise ValueError("Brakuje kluczy API w pliku .env")

def get_plaid_client():
    """
    Tworzy i zwraca klienta PlaidApi z wszystkimi dostępnymi metodami API.
    """

    # Pobranie środowiska z .env (domyślnie 'sandbox')
    plaid_environment = os.getenv("PLAID_ENV", "sandbox")

    # Mapowanie środowiska na hosta
    plaid_host_urls = {
    "sandbox": "https://sandbox.plaid.com",
    "development": "https://development.plaid.com",
    "production": "https://production.plaid.com"
    }

    # Konfiguracja klienta
    configuration = Configuration(
        host=plaid_host_urls[plaid_environment],
        api_key={
            "clientId": os.getenv("PLAID_CLIENT_ID"),
            "secret": os.getenv("PLAID_SECRET")
            }
    )

    # Utworzenie klienta API
    api_client = ApiClient(configuration)

    # Zwrócenie klienta PlaidApi z wszystkimi metodami
    return PlaidApi(api_client)
print("Działa")

plaid_client = get_plaid_client()
print(plaid_client)

print("CLIENT_ID:", os.getenv("PLAID_CLIENT_ID"))
print("SECRET:", os.getenv("PLAID_SECRET"))