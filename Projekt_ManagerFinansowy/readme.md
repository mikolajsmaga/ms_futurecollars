Finance Manager – Plaid Integration
Opis projektu

Finance Manager to aplikacja webowa zbudowana w Pythonie i Flask, która pozwala użytkownikom na integrację danych bankowych przez Plaid API.
Funkcjonalności obejmują:

Połączenie z kontami bankowymi w trybie Sandbox Plaid

Wymiana public_token na access_token

Pobieranie kont użytkownika

Pobieranie transakcji z ostatnich 30 dni

Zapis tokenów w lokalnej bazie SQLite oraz pliku tokens.json

Projekt powstał w ramach ćwiczenia z integracji API i zarządzania danymi finansowymi.

Technologie

Backend: Python 3.13, Flask

Baza danych: SQLite

Pliki JSON: lokalne przechowywanie tokenów

API: Plaid (Sandbox)

Frontend: prosty HTML/JS (Bootstrap planowany w kolejnej fazie)

Instalacja i uruchomienie

Sklonuj repozytorium:

git clone <repo_url>
cd projekt_managerfinansowy


Utwórz i aktywuj środowisko wirtualne:

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux / Mac


Zainstaluj wymagane paczki:

pip install -r requirements.txt


Utwórz plik .env z kluczami Plaid Sandbox:

PLAID_CLIENT_ID=your_client_id
PLAID_SECRET=your_secret
PLAID_ENV=sandbox


Uruchom aplikację Flask:

flask --app app run


Otwórz przeglądarkę i sprawdź endpointy lokalnie (np. http://127.0.0.1:5000/api/accounts)

Dostępne endpointy
Endpoint	Metoda	Opis
/api/sandbox/public_token/exchange	GET	Generuje sandbox public_token, wymienia na access_token i zapisuje tokeny w SQLite i JSON
/api/accounts	GET	Pobiera listę kont użytkownika
/api/transactions	GET	Pobiera transakcje użytkownika z ostatnich 30 dni
/api/token	GET	Podgląd zapisanych tokenów w SQLite i JSON
Struktura projektu
projekt_managerfinansowy/
│
├─ app.py                  # Główny plik Flask
├─ database.py             # Obsługa SQLite
├─ storage.py              # Obsługa JSON
├─ services/
│   └─ plaid_client.py     # Konfiguracja klienta Plaid
├─ tokens.json             # Lokalny zapis tokenów
├─ tokens.db               # Baza danych SQLite
├─ static/                 # CSS, JS (frontend)
└─ templates/              # HTML (frontend)

Użycie

Wygeneruj token Sandbox (GET /api/sandbox/public_token/exchange)

Sprawdź zapis tokenów w tokens.json i SQLite

Pobierz konta użytkownika (GET /api/accounts)

Pobierz transakcje użytkownika (GET /api/transactions)

Notatki

Sandbox generuje transakcje tylko dla ostatnich 30 dni

Daty w SQLite i JSON zapisane w UTC+2

Frontend będzie uzupełniony w kolejnej fazie