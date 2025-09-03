"""TEST PLAID SDK"""
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from plaid.api.plaid_api import PlaidApi

config = Configuration(host="https://sandbox.plaid.com", api_key={"clientId":"...", "secret":"..."})
client = ApiClient(config)
plaid = PlaidApi(client)
print("Plaid SDK działa ✅")