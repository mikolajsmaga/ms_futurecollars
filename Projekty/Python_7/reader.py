#----URUCHAMIANIE TYLKO Z TERMINALA!!!----#

import datetime     # Import biblioteki do obsługi daty i czasu (w tym kodzie nie jest jeszcze używana)
import sys          # Import modułu do obsługi argumentów wiersza poleceń
import csv          # Import modułu do czytania i zapisywania plików CSV

# Pobieramy listę argumentów przekazanych do programu (pomijając nazwę skryptu)
arguments = sys.argv[1:]
print(arguments)  # Wyświetlamy argumenty dla debugowania (można usunąć lub zakomentować później)

# Przypisujemy argumenty do zmiennych:
input_file = arguments[0]   # Pierwszy argument - nazwa pliku wejściowego CSV
output_file = arguments[1]  # Drugi argument - nazwa pliku wyjściowego CSV
changes = arguments[2:]     # Pozostałe argumenty - lista zmian do wprowadzenia, np. ['0,0,gitara', '3,1,kubek']

# Funkcja, która wczytuje plik CSV, aplikuje zmiany i zwraca zmodyfikowaną listę danych
def apply_changes(input_file, changes):
    # Otwieramy plik CSV do odczytu z ustawionym kodowaniem UTF-8 i bez dodatkowych nowych linii
    with open(input_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)             # Tworzymy czytnik CSV, który iteruje po wierszach
        data = [row for row in reader]        # Wczytujemy wszystkie wiersze do listy list (macierz danych)

    # Przechodzimy po każdej zmianie podanej jako string "x,y,nowa_wartosc"
    for change in changes:
        x_str, y_str, new_value = change.split(",")  # Dzielimy string na kolumna, wiersz i nową wartość
        x = int(x_str)       # Zamieniamy numer kolumny na int (indeks kolumny)
        y = int(y_str)       # Zamieniamy numer wiersza na int (indeks wiersza)
        data[y][x] = new_value  # Podmieniamy wartość w odpowiedniej komórce macierzy

    return data  # Zwracamy zmodyfikowaną macierz danych

# Funkcja zapisująca zmodyfikowaną macierz danych do pliku CSV
def save_to_csv(output_file, data):
    # Otwieramy plik do zapisu, z kodowaniem UTF-8 i bez dodatkowych pustych linii
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)       # Tworzymy obiekt writer do zapisu CSV
        writer.writerows(data)          # Zapisujemy wszystkie wiersze (listę list) do pliku

# Główna część programu - tu wywołujemy nasze funkcje w odpowiedniej kolejności
data = apply_changes(input_file, changes)  # Wczytujemy dane i aplikujemy zmiany

# Wyświetlamy w terminalu zmodyfikowany plik (jako linie tekstu rozdzielone przecinkami)
for row in data:
    print(",".join(row))

save_to_csv(output_file, data)  # Zapisujemy wynik do pliku wyjściowego