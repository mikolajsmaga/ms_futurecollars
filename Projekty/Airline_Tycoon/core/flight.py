class Flight:
    def __init__(self, flight_number, airline, plane=None, steward=None):
        # Inicjalizuje lot z numerem lotu i przypisaną linią lotniczą
        self.flight_number = flight_number
        self.airline = airline
        self.passengers = []
        self.plane = None
        self.steward = None


    # metoda przypisująca samolot do lotu
    def assign_plane(self, plane):
        self.plane = plane

    def add_passenger(self, passenger):
        # Sprawdź limit pojemności
        if len(self.passengers) >= self.plane.capacity:
            print("Samolot jest pełny! Nie można dodać więcej pasażerów.")
            return False

        # Sprawdza czy pasażer już jest na liście
        for p in self.passengers:
            if p.first_name == passenger.first_name and p.last_name == passenger.last_name:
                print(f"Pasażer {p.first_name} {p.last_name} już znajduje się na pokładzie.")
                return False

        # Sprawdza czy miejsce jest już zajęte
        for p in self.passengers:
            if p.seat_number == passenger.seat_number:
                print(f"Miejsce {passenger.seat_number} jest już zajęte.")
                return False

        # Jeśli wszystko ok – dodaj pasażera
        self.passengers.append(passenger)
        print(f"Pasażer {passenger.first_name} {passenger.last_name} został dodany.")
        return True

    def remove_passenger(self, passenger):
        # Usuwa pasażera z listy, jeśli znajduje się na pokładzie
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"Pasażer {passenger} został usunięty z lotu.")
        else:
            print(f"Pasażer {passenger} nie znajduje się na tym locie.")

    def list_passengers(self):
        # Wyświetla listę pasażerów przypisanych do lotu
        if self.passengers:
            print(f"Pasażerowie na pokładzie lotu {self.flight_number}: ")
            for passenger in self.passengers:
                print(f" - {passenger}")
        else:
            print(f"Brak pasażerów przypisanych do lotu {self.flight_number}.")

    def change_passenger_seat(self, passenger, new_seat):
        # Sprawdza, czy miejsce jest już zajęte
        for p in self.passengers:
            if p.seat_number == new_seat:
                print(f"Miejsce {new_seat} jest już zajęte.")
                return False
        # Zmienia miejsce pasażera
        passenger.change_seat(new_seat)
        print(f"{passenger.first_name} {passenger.last_name} zmienił miejsce na {new_seat}.")
        return True

    def change_plane(self, new_plane):
        self.plane = new_plane

    def change_flight_number(self, new_flight_number):
        # Sprawdzamy, czy lotnisko lub linia lotnicza już ma ten numer
        if new_flight_number in self.airline.flights:
            print(f"UWAGA!: Lot o numerze {new_flight_number} już istnieje w linii {self.airline.name}.")
            return False

        # Usuwamy stary wpis z linii lotniczej
        del self.airline.flights[self.flight_number]

        # Aktualizujemy numer lotu
        self.flight_number = new_flight_number

        # Dodajemy nowy wpis z nowym numerem
        self.airline.flights[new_flight_number] = self

        print(f"Zmieniono numer lotu na {new_flight_number}")
        return True

    def reassign_steward(self, new_flight_steward):
        self.steward = new_flight_steward
    
    def __repr__(self):
        # Zwraca reprezentację tekstową lotu
        return f"Lot nr.:{self.flight_number} ({self.airline})"

