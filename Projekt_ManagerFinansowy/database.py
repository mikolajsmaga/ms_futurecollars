"""SQLITE - BAZA DANYCH"""
import sqlite3  # biblioteka do obsługi bazy SQLite
from datetime import datetime  # do zapisu daty i czasu

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

    connection.commit()  # zatwierdzenie zmian
    connection.close()   # zamknięcie połączenia z bazą

def save_user_token(user_id, access_token, item_id):
    """
    Zapisuje token użytkownika do bazy danych.
    Jeśli użytkownik już istnieje – nadpisuje dane.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Wstawienie lub nadpisanie danych użytkownika
    cursor.execute("""
        INSERT OR REPLACE INTO tokens (user_id, access_token, item_id, saved_at)
        VALUES (?, ?, ?, ?)
    """, (
        user_id,
        access_token,
        item_id,
        datetime.utcnow().isoformat() + "Z"  # zapis daty w formacie ISO (UTC)
    ))

    connection.commit()
    connection.close()

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
        return {
            "access_token": result[0],
            "item_id": result[1],
            "saved_at": result[2]
        }

    return None