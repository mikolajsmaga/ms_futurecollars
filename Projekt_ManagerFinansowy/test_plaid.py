"""TEST PLAID SDK"""
from plaid import Configuration, ApiClient
from plaid.api.plaid_api import PlaidApi

print("✅ Plaid SDK jest poprawnie zainstalowany i import działa")

try:
    # konfiguracja podstawowa (testowa, bez prawdziwych kluczy)
    configuration = Configuration(
        host="https://sandbox.plaid.com",
        api_key={
            "clientId": "DUMMY_CLIENT_ID",
            "secret": "DUMMY_SECRET"
        }
    )

    api_client = ApiClient(configuration)
    plaid_client = PlaidApi(api_client)

    print("✅ Plaid SDK działa i klient został poprawnie utworzony")

except Exception as e:
    print("❌ Błąd podczas testu Plaid:", e)