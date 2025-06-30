import json
import pickle
import csv
from abc import ABC, abstractmethod  # poprawny import ABC i abstractmethod


class FileHandler(ABC):
    def __init__(self, input_file, output_file, changes):
        """
        Konstruktor bazowy:
        - input_file: ścieżka do pliku wejściowego
        - output_file: ścieżka do pliku wyjściowego
        - changes: lista zmian w formacie ["x,y,wartosc"]
        """
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.data = []  # tutaj będą dane wczytane z pliku

    @abstractmethod  # wymuszamy implementację w klasach dziedziczących
    def load_data(self):
        """Wczytaj dane z pliku wejściowego"""
        pass

    @abstractmethod
    def save_data(self):
        """Zapisz dane do pliku wyjściowego"""
        pass

    @abstractmethod
    def display_data(self):
        """Wyświetl dane w terminalu"""
        pass

    def apply_changes(self):
        """
        Uniwersalna metoda:
        Wprowadza zmiany do danych na podstawie self.changes.
        Zakłada, że self.data to lista list (macierz).
        """
        for change in self.changes:
            try:
                # Rozdzielamy argument na x, y i nową wartość
                x_str, y_str, new_value = change.split(",")
                x = int(x_str)  # kolumna
                y = int(y_str)  # wiersz

                # Sprawdzamy czy indeksy mieszczą się w danych
                if y < len(self.data) and x < len(self.data[y]):
                    self.data[y][x] = new_value  # Wprowadzamy zmianę
                else:
                    print(f"[UWAGA] Nieprawidłowy indeks: ({x},{y}) - zmiana pominięta.")
            except ValueError:
                print(f"[BŁĄD] Zmiana {change} ma niepoprawny format - pominięta.")


# Handler CSV
class CSVHandler(FileHandler):
    def load_data(self):
        """Wczytaj dane z pliku CSV do listy list (macierzy)."""
        with open(self.input_file, encoding='utf-8') as file:
            reader = csv.reader(file)
            temp_matrix = []
            for row in reader:
                temp_row = []
                for cell in row:
                    temp_row.append(cell)  # Nie wymuszamy int, bo może być tekst
                temp_matrix.append(temp_row)
        self.data = temp_matrix  # zapisujemy do atrybutu klasy

    def save_data(self):
        """Zapisz dane do pliku CSV."""
        with open(self.output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

    def display_data(self):
        """Wyświetl dane w terminalu w formacie CSV."""
        for row in self.data:
            print(",".join(row))


# Handler JSON
class JSONHandler(FileHandler):
    def load_data(self):
        """Wczytaj dane z pliku JSON."""
        with open(self.input_file, encoding='utf-8') as file:
            self.data = json.load(file)

    def save_data(self):
        """Zapisz dane do pliku JSON z formatowaniem."""
        with open(self.output_file, 'w+', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def display_data(self):
        """Wyświetl dane JSON jako ładnie sformatowany tekst."""
        print(json.dumps(self.data, indent=4))


# Handler PICKLE
class PICKLEHandler(FileHandler):
    def load_data(self):
        """Wczytaj dane z pliku pickle."""
        with open(self.input_file, 'rb') as file:
            return pickle.load(file)

    def save_data(self):
        """Zapisz dane do pliku pickle."""
        with open(self.output_file, 'wb') as file:
            file.write(pickle.dumps(self.data))

    def display_data(self):
        """Wyświetl dane pickle przez wypisanie ich typu i zawartości."""
        print(self.data)


# Handler TXT - zostawiamy puste implementacje na razie
class TXTHandler(FileHandler):
    def load_data(self):
        with open(self.input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # Zamieniamy linie na listę list, gdzie każda linia jest listą z jednym stringiem
        self.data = [[line.strip()] for line in lines]

    def save_data(self):
        with open(self.output_file, 'w', encoding='utf-8') as file:
            for row in self.data:
                file.write(row[0] + "\n")

    def display_data(self):
        for row in self.data:
            print(row[0])