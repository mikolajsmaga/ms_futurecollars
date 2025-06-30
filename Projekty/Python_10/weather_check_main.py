from datetime import datetime, timedelta
from weather_utility import check_rain_status
#from weather_check_file_handler import FileHandler
from weather_forecast import WeatherForecast
from geopy.geocoders import Nominatim
import requests

# Inicjalizacja obsługi pliku
#file_handler = FileHandler("weather_data_read.json")
weather_forecast = WeatherForecast("weather_data_read.json")

# Pobieramy nazwę miasta od użytkownika
city = input("Podaj swoje miasto: ")

# Pętla do pobrania poprawnej daty lub domyślnie jutrzejszej
while True:
    date = input("Podaj datę w formacie YYYY-MM-DD (lub zostaw puste dla jutrzejszej daty): ")
    if not date:
        # Jeśli puste, ustawiamy jutro
        date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    try:
        # Sprawdzamy, czy data ma poprawny format
        datetime.strptime(date, "%Y-%m-%d")
        break  # jeśli OK, wychodzimy z pętli
    except ValueError:
        print("Niepoprawny format daty. Spróbuj ponownie.")

# Sprawdzamy, czy prognoza na dany dzień i miasto jest już w pliku (klucze: miasto, data)
result = weather_forecast[city, date]

if result != "Data not found":
    # Jeśli mamy dane lokalnie, wyświetlamy je
    print(f"Wynik z pliku: {result}")
else:
    # Jeśli brak danych, pobieramy z API i od razu zapisujemy do pliku
    rain = check_rain_status(city, date)
    weather_forecast[city, date] = rain  # aktualizujemy lokalny słownik
    print(f"Wynik z API: {rain}")

# Pokazujemy finalny wynik (jako podsumowanie)
print(f"Dla miasta {city} w dniu {date}: {weather_forecast[city, date]}")

# Opcjonalne: pobieramy i wyświetlamy dokładną lokalizację miasta przez geopy
geolocator = Nominatim(user_agent="mikola_smaga_app")
location = geolocator.geocode(city)

if location:
    print(location.address)
    print((location.latitude, location.longitude))
    # print(location.raw)  # Odkomentuj, jeśli chcesz pełne dane lokalizacyjne
else:
    print("Nie udało się znaleźć lokalizacji dla podanego miasta.")