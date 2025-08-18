import csv

def task_1(search, data):
    #1 Split data for lines
    lines = data.splitlines()
    header_line = lines[0]
    header = header_line.split(",")

    #2 Prepare rows for data
    rows = []
    for line in lines[1:]:         # Skip header
        row = line.split(",")      # dzielimy wartości w wierszu
        rows.append(row)           # dodajemy wiersz do listy

    # Na razie zwracamy wszystkie wiersze, żeby zobaczyć efekt
    return rows

data = "side,currency,value\nIN,PLN,1\nIN,EUR,2\nOUT,ANY,3"
print(task_1({'side': 'IN', 'currency': 'PLN'}, data))