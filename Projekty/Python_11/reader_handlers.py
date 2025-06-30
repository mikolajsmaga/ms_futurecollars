import json
import pickle
import csv
from abc import ABC, abstractmethod


class FileHandler(ABC):
    """
    Klasa bazowa obsługująca ogólny interfejs dla różnych formatów plików.
    """

    def __init__(self, input_file, output_file, changes):
        # Inicjalizacja ścieżek do plików i listy zmian
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.data = []  # Tutaj będą przechowywane dane wczytane z pliku

    @abstractmethod
    def load_data(self):
        # Abstrakcyjna metoda do wczytania danych z pliku
        pass

    @abstractmethod
    def save_data(self):
        # Abstrakcyjna metoda do zapisania danych do pliku
        pass

    @abstractmethod
    def display_data(self):
        # Abstrakcyjna metoda do wyświetlenia danych w terminalu
        pass

    def apply_changes(self):
        """
        Metoda wprowadzająca zmiany do danych na podstawie listy self.changes.
        Zakłada, że self.data to lista list (czyli macierz).
        """
        for change in self.changes:
            try:
                # Rozdzielamy ciąg znaków 'x,y,nowa_wartosc' na trzy części
                col_str, row_str, new_value = change.split(",")
                # Konwertujemy indeksy kolumny i wiersza na liczby całkowite
                col_index = int(col_str)
                row_index = int(row_str)

                # Sprawdzamy, czy podane indeksy mieszczą się w granicach danych
                if row_index < len(self.data) and col_index < len(self.data[row_index]):
                    # Wprowadzamy nową wartość do odpowiedniej komórki
                    self.data[row_index][col_index] = new_value
                else:
                    # Jeśli indeksy są niepoprawne - wyświetlamy ostrzeżenie i pomijamy zmianę
                    print(f"[UWAGA] Nieprawidłowy indeks: ({col_index},{row_index}) - zmiana pominięta.")
            except ValueError:
                # Obsługa błędu, gdy format zmiany jest niepoprawny (np. brak przecinków)
                print(f"[BŁĄD] Zmiana {change} ma niepoprawny format - pominięta.")


class CsvHandler(FileHandler):
    """
    Handler plików CSV.
    """

    def load_data(self):
        # Otwieramy plik CSV do odczytu
        with open(self.input_file, encoding="utf-8") as file:
            reader = csv.reader(file)
            # Tworzymy listę list, każda podlista to wiersz w CSV
            self.data = [row for row in reader]

    def save_data(self):
        # Otwieramy plik CSV do zapisu
        with open(self.output_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Zapisujemy wszystkie wiersze do pliku
            writer.writerows(self.data)

    def display_data(self):
        # Wyświetlamy każdy wiersz oddzielony przecinkami
        for row in self.data:
            print(",".join(row))


class JsonHandler(FileHandler):
    """
    Handler plików JSON.
    """

    def load_data(self):
        # Otwieramy plik JSON i wczytujemy zawartość jako strukturę Pythona (listę/dict)
        with open(self.input_file, encoding="utf-8") as file:
            self.data = json.load(file)

    def save_data(self):
        # Zapisujemy dane do pliku JSON z ładnym formatowaniem (wcięcia)
        with open(self.output_file, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)

    def display_data(self):
        # Wyświetlamy dane JSON w czytelnej formie (formatowanie)
        print(json.dumps(self.data, indent=4))


class PickleHandler(FileHandler):
    """
    Handler plików Pickle (serializacja binarna).
    """

    def load_data(self):
        # Otwieramy plik binarny i ładujemy obiekt z pickle
        with open(self.input_file, "rb") as file:
            self.data = pickle.load(file)

    def save_data(self):
        # Zapisujemy obiekt do pliku binarnego pickle
        with open(self.output_file, "wb") as file:
            pickle.dump(self.data, file)

    def display_data(self):
        # Wyświetlamy typ danych oraz zawartość (do debugowania)
        print(f"[PICKLE] typ danych: {type(self.data)}")
        print(self.data)


class TxtHandler(FileHandler):
    """
    Handler zwykłych plików tekstowych (każda linia to osobny wiersz).
    """

    def load_data(self):
        # Otwieramy plik tekstowy i wczytujemy wszystkie linie
        with open(self.input_file, encoding="utf-8") as file:
            lines = file.readlines()
            # Tworzymy listę list, każda linia jako jedna wartość w podliście
            self.data = [[line.strip()] for line in lines]

    def save_data(self):
        # Zapisujemy dane linia po linii do pliku tekstowego
        with open(self.output_file, "w", encoding="utf-8") as file:
            for row in self.data:
                file.write(row[0] + "\n")

    def display_data(self):
        # Wyświetlamy zawartość wczytanego pliku linia po linii
        for row in self.data:
            print(row[0])