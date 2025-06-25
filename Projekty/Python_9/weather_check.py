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

# Sprawdzenie, czy dane są już w pliku
city_info = file_handler[city, date]

if city_info != "Data not found":
    print("Wynik z pliku:", city_info)
else:
    # Funkcja do pobrania danych z API – musisz ją jeszcze zdefiniować
    rain_sum = check_rain_status(city, date)

    # Zapisujemy nowy wynik
    file_handler[city, date] = rain_sum
    file_handler.write_to_file()
    print("Wynik z API:", rain_sum)

#Mozliwosc testow
# geolocator = Nominatim(user_agent="mikola_smaga_app")
# location = geolocator.geocode(city)
# print(location.address)
# print((location.latitude, location.longitude))
# print(location.raw)
