#___URUCHAMIAMY TYLKO Z TERMINALA___#
import sys
from reader_handlers import FileHandler, CsvHandler, TxtHandler, PickleHandler, JsonHandler

def get_handler(file_path, changes):
    """Zwraca odpowiedni handler na podstawie rozszerzenia pliku."""
    if file_path.endswith('.csv'):
        return CsvHandler(input_file=file_path, output_file=None, changes=changes)
    elif file_path.endswith('.json'):
        return JsonHandler(input_file=file_path, output_file=None, changes=changes)
    elif file_path.endswith('.txt'):
        return TxtHandler(input_file=file_path, output_file=None, changes=changes)
    elif file_path.endswith('.pkl'):
        return PickleHandler(input_file=file_path, output_file=None, changes=changes)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

def main():
    arguments = sys.argv[1:]
    if len(arguments) < 2:
        print("Usage: program.py input_file output_file [changes...]")
        sys.exit(1)

    input_file = arguments[0]
    output_file = arguments[1]
    changes = arguments[2:]

    # Tworzymy handler do wczytania danych
    handler = get_handler(input_file, changes)
    handler.output_file = output_file  # ustawiamy plik wyjściowy
    handler.load_data()                # wczytujemy dane
    handler.apply_changes()            # wprowadzamy zmiany
    handler.display_data()             # wyświetlamy wynik (opcjonalnie)
    handler.save_data()                # zapisujemy wynik

if __name__ == "__main__":
    main()



