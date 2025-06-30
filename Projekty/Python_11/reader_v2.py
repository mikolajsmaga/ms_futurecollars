#----URUCHAMIANIE TYLKO Z TERMINALA!!!----#

#import datetime    # Import biblioteki do obsługi daty i czasu (w tym kodzie nie jest jeszcze używana)
import sys          # Import modułu do obsługi argumentów wiersza poleceń
import csv          # Import modułu do czytania i zapisywania plików CSV
import abc          # Import modułu abstrakcyjne metody

class CSVEditor:
    def __init__(self, input_file, output_file, changes):
        """Konstruktor: zapisuje nazwy plików i listę zmian"""
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.data = []  # Tu wczytamy dane z pliku

    def load_data(self):
        # Otwieramy plik CSV do odczytu z ustawionym kodowaniem UTF-8 i bez dodatkowych nowych linii
        with open(input_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)  # Tworzymy czytnik CSV, który iteruje po wierszach
            data = [row for row in reader]  # Wczytujemy wszystkie wiersze do listy list (macierz danych)

    def apply_changes(self):
        """Zastosuj zmiany do danych w self.data"""
        for change in self.changes:
            x_str, y_str, new_value = change.split(",")
            x = int(x_str)
            y = int(y_str)
            if y < len(self.data) and x < len(self.data[y]):  # Sprawdzamy czy indeks nie wyjdzie poza macierz
                self.data[y][x] = new_value
            else:
                print(f"[UWAGA] Nieprawidłowy indeks: ({x}, {y}) - zmiana pominięta.")

    def save_data(self):
        """Zapisz zmodyfikowane dane do pliku wyjściowego"""
        with open(self.output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)

    def display_data(self):
        """Wyświetl dane na ekranie"""
        for row in self.data:
            print(",".join(row))

if __name__ == "__main__":
    # Pobieramy argumenty z terminala
    arguments = sys.argv[1:]
    print(arguments)

    input_file = arguments[0]
    output_file = arguments[1]
    changes = arguments[2:]

    # Tworzymy obiekt klasy CSVEditor
    editor = CSVEditor(input_file, output_file, changes)

    # Wykonujemy operacje
    editor.load_data()
    editor.apply_changes()
    editor.display_data()
    editor.save_data()

