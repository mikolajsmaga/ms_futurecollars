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

# # Pobieramy listę argumentów przekazanych do programu (pomijając nazwę skryptu)
# arguments = sys.argv[1:]
# print(arguments)  # Wyświetlamy argumenty dla debugowania (można usunąć lub zakomentować później)
#
# # Przypisujemy argumenty do zmiennych:
# input_file = arguments[0]   # Pierwszy argument - nazwa pliku wejściowego CSV
# output_file = arguments[1]  # Drugi argument - nazwa pliku wyjściowego CSV
# changes = arguments[2:]     # Pozostałe argumenty - lista zmian do wprowadzenia, np. ['0,0,gitara', '3,1,kubek']
#
# # Funkcja, która wczytuje plik CSV, aplikuje zmiany i zwraca zmodyfikowaną listę danych
# def apply_changes(input_file, changes):
#     # Otwieramy plik CSV do odczytu z ustawionym kodowaniem UTF-8 i bez dodatkowych nowych linii
#     with open(input_file, newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)             # Tworzymy czytnik CSV, który iteruje po wierszach
#         data = [row for row in reader]        # Wczytujemy wszystkie wiersze do listy list (macierz danych)
#
#     # Przechodzimy po każdej zmianie podanej jako string "x,y,nowa_wartosc"
#     for change in changes:
#         x_str, y_str, new_value = change.split(",")  # Dzielimy string na kolumna, wiersz i nową wartość
#         x = int(x_str)       # Zamieniamy numer kolumny na int (indeks kolumny)
#         y = int(y_str)       # Zamieniamy numer wiersza na int (indeks wiersza)
#         data[y][x] = new_value  # Podmieniamy wartość w odpowiedniej komórce macierzy
#
#     return data  # Zwracamy zmodyfikowaną macierz danych
#
# # Funkcja zapisująca zmodyfikowaną macierz danych do pliku CSV
# def save_to_csv(output_file, data):
#     # Otwieramy plik do zapisu, z kodowaniem UTF-8 i bez dodatkowych pustych linii
#     with open(output_file, 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)       # Tworzymy obiekt writer do zapisu CSV
#         writer.writerows(data)          # Zapisujemy wszystkie wiersze (listę list) do pliku
#
# # Główna część programu - tu wywołujemy nasze funkcje w odpowiedniej kolejności
# data = apply_changes(input_file, changes)  # Wczytujemy dane i aplikujemy zmiany
#
# # Wyświetlamy w terminalu zmodyfikowany plik (jako linie tekstu rozdzielone przecinkami)
# for row in data:
#     print(",".join(row))
#
# save_to_csv(output_file, data)  # Zapisujemy wynik do pliku wyjściowego