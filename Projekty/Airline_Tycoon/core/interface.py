from .passenger import Passenger  # Import klasy Passenger z modułu passenger

class MainMenu:
    def __init__(self, airport):
        self.airport = airport  # Przechowuje referencję do obiektu Airport

    def display_menu(self):
        # Wyświetla menu główne w konsoli
        print("\n--- MENU GŁÓWNE ---")
        print("1. Pokaż linie lotnicze")
        print("2. Pokaż loty")
        print("3. Pokaż pasażerów")
        print("4. Dodaj pasażera")
        print("5. Wyjdź")

    def run(self):
        # Główna pętla programu, czeka na wybór użytkownika i wykonuje akcje
        while True:
            self.display_menu()  # Wyświetl menu
            choice = input("Wybierz opcję: ")  # Pobierz wybór użytkownika

            match choice:  # Dopasowanie wyboru do odpowiedniej akcji
                case "1":
                    # Wyświetl listę linii lotniczych na lotnisku
                    print("Linie lotnicze:", self.airport.airlines)
                case "2":
                    # Wyświetl listę lotów
                    print("Loty:", self.airport.flights)
                case "3":
                    # Wyświetl listę pasażerów
                    print("Pasażerowie:", self.airport.passengers)
                case "4":
                    # Dodaj nowego pasażera
                    first_name = input("Imię pasażera: ")
                    last_name = input("Nazwisko pasażera: ")
                    flight_number = input("Numer lotu: ")
                    seat_number = input("Numer miejsca: ")

                    # Tworzymy nowy obiekt Passenger
                    p = Passenger(first_name, last_name, flight_number, seat_number)

                    # Szukamy lotu o podanym numerze w liście lotów lotniska
                    flight = None
                    for f in self.airport.flights:
                        if f.flight_number == flight_number:
                            flight = f  # Zapisujemy znaleziony lot
                            break

                    if flight:
                        # Próba dodania pasażera do lotu, sprawdzamy czy się udało
                        if flight.add_passenger(p):
                            # Jeśli dodanie powiodło się, dodajemy też pasażera do lotniska
                            self.airport.add_passenger(p)
                            print(f"Dodano pasażera: {p.first_name} {p.last_name} do lotu {flight_number}")
                        else:
                            # Informacja o błędzie (np. miejsce zajęte lub samolot pełny)
                            print("Nie udało się dodać pasażera do lotu (możliwe miejsce zajęte lub samolot pełny).")
                    else:
                        # Jeśli nie znaleziono lotu o podanym numerze
                        print("Nie znaleziono lotu o podanym numerze.")
                case "5":
                    # Zakończenie programu
                    print("Koniec programu.")
                    break
                case _:
                    # Obsługa nieznanych opcji
                    print("Nieznana opcja, spróbuj ponownie.")