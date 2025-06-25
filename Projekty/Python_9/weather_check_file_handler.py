import json
import os

class FileHandler:
    def __init__(self, file_path):
        # Inicjalizacja obiektu z podaną ścieżką do pliku JSON
        self.file = file_path
        self.data = self.read_data_from_file()
        self.iterator = iter(self.data.items())

    def read_data_from_file(self):
        # Sprawdzamy, czy plik istnieje
        if not os.path.exists(self.file):
            # Jeśli plik nie istnieje, zwracamy pusty słownik
            return {}

        try:
            # Otwieramy plik do odczytu
            with open(self.file, 'r') as file:
                # Wczytujemy dane JSON jako słownik
                return json.load(file)
        except json.JSONDecodeError:
            # Jeśli plik jest pusty lub zawiera błędny JSON,
            # zwracamy pusty słownik zamiast wywołać błąd
            return {}

    def __getitem__(self, item):
        # Umożliwia dostęp do danych jak w słowniku
        # np. handler["Warszawa", "2025-06-24"]
        city, date = item
        return self.data.get(city, {}).get(date, "Data not found")

    def __setitem__(self, key, value):
        # Ustawia wartość (np. suma opadów) dla danego miasta i daty
        city, date = key
        if city in self.data:
            self.data[city][date] = value
        else:
            self.data[city] = {}
            self.data[city][date] = value

    def write_to_file(self):
        # Zapisuje aktualne dane z pamięci do pliku JSON
        with open(self.file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def items(self):
        # Generator – iteruje po wszystkich wpisach w formacie:
        # (miasto, data, wartość)
        for city, date_dict in self.data.items():
            for date_value, rain_info in date_dict.items():
                yield city, date_value, rain_info

    def __iter__(self):
        # Wspiera iterację obiektu FileHandler
        return self

    def __next__(self):
        # Pozwala na użycie w pętli for
        return next(self.iterator)