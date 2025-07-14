class Airline:
    def __init__(self, name: str, flights=None):
        # Inicjalizujemy linię lotniczą z nazwą i słownikiem lotów
        # Jeśli nie podano lotów, ustawiamy pusty słownik
        self.name = name
        self.flights = flights if flights is not None else {}

    def add_flight(self, flight_obj):
        # Sprawdzamy, czy numer lotu już istnieje w słowniku
        if flight_obj.flight_number in self.flights:
            print(f"UWAGA!: Lot o numerze {flight_obj.flight_number} już istnieje w bazie {self.name}.")
            return False
        # Dodajemy lot do słownika
        self.flights[flight_obj.flight_number] = flight_obj
        return True

    def find_flight(self, flight_number):
        # Zwracamy lot po numerze lub None, jeśli nie znaleziono
        return self.flights.get(flight_number, None)

    def remove_flight(self, flight_number):
        # Usuwamy lot z listy, jeśli istnieje, zwracamy True, w przeciwnym razie False
        if flight_number in self.flights:
            del self.flights[flight_number]
            return True
        return False

    def change_airline_name(self, new_name):
        # Zmiana nazwy linii lotniczej
        self.name = new_name

    def change_flight_number(self, old_number, new_number):
        # Zmienia numer lotu, aktualizując klucz w słowniku flights
        if old_number in self.flights:
            flight = self.flights[old_number]
            flight.change_flight_number(new_number) # Zmiana numeru w obiekcie wewnątrz
            self.flights[new_number] = flight       # Dodanie nowego klucza
            del self.flights[old_number]            # Usunięcie starego klucza
            return True
        return False

    def __repr__(self):
        # Reprezentacja tekstowa z nazwą i liczbą lotów
        return f"{self.name} ({len(self.flights)} lotów) - numery lotów: {list(self.flights.keys())}"