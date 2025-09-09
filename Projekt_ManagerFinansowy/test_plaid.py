"""TEST PLAID SDK"""
from services.plaid_client import get_plaid_client
import os

# Sprawdzenie, czy klient w ogóle ładuje zmienne
print("CLIENT_ID:", os.getenv("PLAID_CLIENT_ID"))
print("SECRET:", os.getenv("PLAID_SECRET"))

# Spróbuj utworzyć klienta Plaid
try:
    client = get_plaid_client()
    print("✅ Klient Plaid utworzony poprawnie")
except Exception as e:
    print("❌ Błąd przy tworzeniu klienta Plaid:", e)