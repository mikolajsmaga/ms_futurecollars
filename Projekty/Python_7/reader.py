import datetime
import sys
import csv

arguments = sys.argv[1:]
print(arguments)

input_file = arguments[0]
output_file = arguments[1]
changes = arguments[2:]  # to będzie lista zmian np. ['0,0,gitara', '3,1,kubek']

def apply_changes(input_file, changes):
    # Otwórz i Wczytaj dane z pliku CSV
    with open(input_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # Zastosuj zmiany
    for change in changes:
        x_str, y_str, new_value = change.split(",")
        x = int(x_str)  # kolumna
        y = int(y_str)  # wiersz
        data[y][x] = new_value
    return data

def save_to_csv(output_file, data):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Główna część programu
data = apply_changes(input_file, changes)
for row in data:
    print(",".join(row))
save_to_csv(output_file, data)