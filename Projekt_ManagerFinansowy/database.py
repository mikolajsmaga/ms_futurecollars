"""SQLITE - BAZA DANYCH"""
import sqlite3
from datetime import datetime

# Nazwa pliku bazy danych
DATABASE_NAME = "tokens.db"

def initialize_database():
    """
    Tworzy bazę danych i tabelę 'tokens', jeśli jeszcze nie istnieje.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Tworzenie tabeli z kolumnami: user_id, access_token, item_id, saved_at
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tokens (
            user_id TEXT PRIMARY KEY,
            access_token TEXT NOT NULL,
            item_id TEXT NOT NULL,
            saved_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    print("DEBUG: Baza SQLite zainicjalizowana")

def save_user_token(user_id, access_token, item_id):
    """
    Zapisuje token użytkownika do bazy danych.
    Jeśli użytkownik już istnieje – nadpisuje dane.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    saved_at = datetime.utcnow().isoformat() + "Z"

    # Wstawienie lub nadpisanie danych użytkownika
    cursor.execute("""
        INSERT INTO tokens (user_id, access_token, item_id, saved_at)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            access_token=excluded.access_token,
            item_id=excluded.item_id,
            saved_at=excluded.saved_at
    """, (user_id, access_token, item_id, saved_at))

    connection.commit()
    connection.close()
    print(f"DEBUG: Zapisano token do SQLite dla {user_id}")

def get_user_token(user_id):
    """
    Pobiera token użytkownika z bazy danych.
    Zwraca słownik z danymi lub None, jeśli użytkownik nie istnieje.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT access_token, item_id, saved_at
        FROM tokens
        WHERE user_id = ?
    """, (user_id,))

    result = cursor.fetchone()
    connection.close()

    if result:
        token_data = {
            "access_token": result[0],
            "item_id": result[1],
            "saved_at": result[2]
        }
        print(f"DEBUG: Odczytano token z SQLite dla {user_id}: {token_data}")
        return token_data

    print(f"DEBUG: Brak tokenu w SQLite dla {user_id}")
    return None