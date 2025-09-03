"""KLIENT PLAID"""
import os
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from plaid.api.plaid_api import PlaidApi

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
    "clientId": os.environ.get("PLAID_CLIENT_ID", "your_client_id_here"),
    "secret": os.environ.get("PLAID_SECRET", "your_secret_here")
    }
    )

    # Utworzenie klienta API
    api_client = ApiClient(configuration)

    # Zwrócenie klienta PlaidApi z wszystkimi metodami
    return PlaidApi(api_client)
print("Działa")