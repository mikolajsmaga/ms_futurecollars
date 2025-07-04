from datetime import datetime, timedelta

from weather_utility import check_rain_status
from weather_check_file_handler import FileHandler
from geopy.geocoders import Nominatim
import requests

# Inicjalizacja obsługi pliku
file_handler = FileHandler("weather_data.json")

# Inputy od użytkownika
city = input("Podaj swoje miasto: ")
#date = input("Podaj datę w formacie YYYY-MM-DD: ")

while True:
    date = input("Podaj datę w formacie YYYY-MM-DD (lub zostaw puste dla jutrzejszej daty): ")
# Jeśli nie podano daty → ustaw jutro
    if not date:
        date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    try:
        # Próba sparsowania daty zgodnie z formatem YYYY-MM-DD
        datetime.strptime(date, "%Y-%m-%d")
        # Jeśli parsowanie się powiodło, data jest poprawna - wychodzimy z pętli
        break
    except ValueError:
        # Jeśli parsowanie się nie powiodło, data jest niepoprawna
        print("Niepoprawny format daty. Spróbuj ponownie.")

# Sprawdzenie, czy prognoza dla miasta i daty jest już zapisana w pliku JSON
city_info = file_handler[city, date]

if city_info != "Data not found":
    # Jeśli dane są dostępne w pliku — wyświetlamy je
    print(f"Dla miasta {city} w dniu {date}: {city_info}")
else:
    # Jeśli danych nie ma — pobieramy je z API przez funkcję z utility
    rain_sum = check_rain_status(city, date)
    # Zapisujemy nowo pobraną prognozę do pliku JSON
    file_handler[city, date] = rain_sum
    file_handler.write_to_file()
    # Wyświetlamy wynik pobrany z API
    print(f"Dla miasta {city} w dniu {date}: {rain_sum}")


#Mozliwosc testow
# geolocator = Nominatim(user_agent="mikola_smaga_app")
# location = geolocator.geocode(city)
# print(location.address)
# print((location.latitude, location.longitude))
# print(location.raw)
