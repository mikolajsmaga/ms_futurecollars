import os
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from plaid.api.accounts import Accounts
from plaid.api.transactions import Transactions
from plaid.api.item import Item

def get_plaid_client():
    """
    Tworzy i zwraca słownik z klientami API:
    - Accounts
    - Transactions
    - Item
    Wszystko na podstawie konfiguracji środowiska.
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
            "clientId": os.environ["PLAID_CLIENT_ID"],
            "secret": os.environ["PLAID_SECRET"]
        }
    )

    # Utworzenie klienta API
    api_client = ApiClient(configuration)

    # Zwrócenie osobnych klientów do każdej części API
    return {
        "accounts": Accounts(api_client),
        "transactions": Transactions(api_client),
        "item": Item(api_client)
    }