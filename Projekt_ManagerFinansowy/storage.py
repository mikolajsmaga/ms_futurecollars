"""JSON - STORAGE"""
import json  # biblioteka do obsługi formatu JSON
from datetime import datetime  # do zapisu aktualnej daty i czasu
from pathlib import Path  # do pracy ze ścieżkami plików

# Ścieżka do pliku, w którym będą zapisane tokeny
TOKENS_FILE_PATH = Path("tokens.json")

def save_token_to_json(user_id, access_token, item_id):
    """
    Zapisuje token użytkownika do pliku JSON.
    Jeśli plik już istnieje – aktualizuje dane użytkownika.
    """
    # Sprawdzenie, czy plik już istnieje
    if TOKENS_FILE_PATH.exists():
        # Wczytanie istniejących danych z pliku
        with TOKENS_FILE_PATH.open("r", encoding="utf-8") as file:
            token_data = json.load(file)
    else:
        # Jeśli plik nie istnieje – tworzymy pusty słownik
        token_data = {}

    # Dodanie lub aktualizacja danych dla danego użytkownika
    token_data[user_id] = {
        "access_token": access_token,
        "item_id": item_id,
        "saved_at": datetime.utcnow().isoformat() + "Z"  # zapis daty w formacie ISO (UTC)
    }

    # Zapis zaktualizowanych danych do pliku
    with TOKENS_FILE_PATH.open("w", encoding="utf-8") as file:
        json.dump(token_data, file, indent=2)

def get_token_from_json(user_id):
    """
    Pobiera token użytkownika z pliku JSON.
    Zwraca słownik z danymi lub None, jeśli użytkownik nie istnieje.
    """
    # Jeśli plik nie istnieje – nie ma danych
    if not TOKENS_FILE_PATH.exists():
        return None

    # Wczytanie danych z pliku
    with TOKENS_FILE_PATH.open("r", encoding="utf-8") as file:
        token_data = json.load(file)

    # Zwrócenie danych dla danego użytkownika (lub None)
    return token_data.get(user_id) or None