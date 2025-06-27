import json
import os
from weather_utility import check_rain_status

class WeatherForecast:
    def __init__(self, file_path):
        self.file_path = file_path  # Zapisuje ścieżkę do pliku JSON
        self.data = self.read_data_from_file()  # Wczytuje dane z pliku do słownika

    def read_data_from_file(self):  # Funkcja odczytująca dane z pliku
        if os.path.exists(self.file_path):  # Jeśli plik istnieje
            with open(self.file_path, "r", encoding="utf-8") as file:  # Otwórz plik do odczytu
                try: # Spróbuj:
                    return json.load(file)  # Wczytaj dane JSON jako słownik {}
                except json.JSONDecodeError:  # Jeśli plik jest niepoprawny
                    return {}  # Zwróć pusty słownik
        else:
            return {}  # Jeśli plik nie istnieje, też zwróć pusty słownik

    def write_data_to_file(self):  # Funkcja zapisująca dane do pliku JSON
        with open(self.file_path, "w",
                  encoding="utf-8") as file:  # Otwiera plik do zapisu w trybie tekstowym z polskim kodowaniem
            json.dump(self.data, file, ensure_ascii=False,
                      indent=4)  # Zapisuje dane jako JSON: nie zamienia polskich znaków, ładnie sformatowane

    def __getitem__(self, key): #Pobieranie wartości (z konkretnego klucza) - GET to ZAPYTANIE CO JEST POD KLUCZEM
        city, date = key
        if city in self.data and date in self.data[city]: #Warunek jeśli wartość jest w data
            return self.data[city][date]  # Zwróć przypisaną pogodę dla tej daty
        else: #Jeśli nie ma:
            return "Data not found"

    def __setitem__(self, key, value): #Ustawianie wartości - SET to POLECENIE, USTAW POD TYM KLUCZEM KONKRETNĄ WARTOŚĆ
        city, date = key #Klucze to (miasto, data)
        if city not in self.data: #SELF.DATA TO SŁOWNIK!
            self.data[city] = {} #Jeśli nie było miasta, tworzy nowe w słowniku czyli plik *.json
        if date in self.data[city]:
            print(f"Uwaga: prognoza dla miasta {city} na dzień {date} została nadpisana.")
        self.data[city][date] = value # Ustawianie: przypisz wartość (np. informacja o pogodzie) pod kluczem (np. datą)
        self.write_data_to_file() # Zapisz zaktualizowany słownik do pliku JSON

    def __iter__(self):
        return iter(self.data)

    def items(self):
        # Iteruj/Przeszukaj po parach (data, pogoda) zapisanych w słowniku self.data
        for date, weather in self.data.items():
            # Zwracaj każdą parę jako tuple (data, pogoda) — używamy generatora
            yield (date, weather)

    def __repr__(self):
        return f"WeatherForecast(file='{self.file_path}', entries={len(self.data)})"