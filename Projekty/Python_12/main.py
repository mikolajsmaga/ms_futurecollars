from order import OrderProcessor
from inventory import InventoryManager
from monitor import monitor

@monitor
def main():
    inventory = InventoryManager()
    processor = OrderProcessor(inventory)

    print("=== System zamówień ===")
    while True:
        product = input("Podaj nazwę produktu (lub 'exit'): ")
        if product.lower() == 'exit':
            break

        try:
            quantity = int(input("Podaj ilość: "))
        except ValueError:
            print("Błąd: ilość musi być liczbą całkowitą.")
            continue


        success = processor.process_order(product, quantity)
        if success:
            print("Zamówienie zrealizowane")
        else:
            print("Brak wystarczającej ilości lub nieznany produkt")

if __name__ == "__main__":
    main()