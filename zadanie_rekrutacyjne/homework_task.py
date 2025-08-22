import csv
from io import StringIO


def task_1(search_keys, csv_data):
    """
    Szukamy pierwszego wiersza w CSV, który pasuje do podanych warunków
    i zwracamy jego wartość z kolumny 'value'.

    Zasady:
    - Jeśli znajdziemy pasujący wiersz, zwracamy jego 'value'
    - Jeśli nic nie pasuje, zwracamy '-1'
    - Jeśli w nagłówku nie ma jakiegoś klucza z search_keys -> błąd "Key mismatch"
    """

    # traktujemy stringa z danymi jak plik
    csv_stream = StringIO(csv_data)

    # wczytujemy dane jako słowniki (kolumna -> wartość)
    csv_reader = csv.DictReader(csv_stream)
    csv_header = csv_reader.fieldnames

    # sprawdzamy czy wszystkie klucze istnieją w nagłówku
    for column_name in search_keys.keys():
        if column_name not in csv_header:
            raise Exception("Key mismatch")

    # szukamy pierwszego pasującego wiersza
    for row in csv_reader:
        match = True
        for column_name, expected_value in search_keys.items():
            # wartości z CSV to stringi, więc porównujemy też jako string
            if row[column_name] != str(expected_value):
                match = False
                break
        if match:
            return row['value']  # zwracamy wartość kolumny 'value'

    # jeśli nic nie znaleziono
    return '-1'


def task_2(key_list, csv_data):
    """
    Liczymy średnią ważoną dla wierszy, które pasują do podanych kluczy.

    Waga:
    - 20 jeśli value jest parzyste
    - 10 jeśli value jest nieparzyste

    Zwracamy wynik zaokrąglony do jednego miejsca po przecinku jako string.
    Jeśli nic nie pasuje -> '-1'.
    """

    # traktujemy stringa z danymi jak plik
    csv_file = StringIO(csv_data)
    reader = csv.DictReader(csv_file)

    # sprawdzamy czy wszystkie klucze istnieją w nagłówku
    for key_dict in key_list:
        for key in key_dict.keys():
            if key not in reader.fieldnames:
                raise ValueError("Key mismatch")

    # zmienne pomocnicze
    total_weighted_value = 0
    total_weight = 0

    # lecimy po każdym wierszu w CSV
    for row in reader:
        # sprawdzamy każdy zestaw kluczy z listy
        for key_dict in key_list:
            match = True
            for key, value in key_dict.items():
                if row[key] != str(value):
                    match = False
                    break
            if match:  # jak wiersz pasuje
                val = int(row['value'])  # pobieramy liczbe z kolumny 'value'
                weight = 20 if val % 2 == 0 else 10
                total_weighted_value += val * weight
                total_weight += weight
                break  # jak już pasuje, to nie sprawdzamy dalej kolejnych słowników

    # obliczamy średnią ważoną
    if total_weight == 0:
        return '-1'
    else:
        weighted_avg = total_weighted_value / total_weight
        return f"{weighted_avg:.1f}"