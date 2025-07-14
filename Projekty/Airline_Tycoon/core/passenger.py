class Passenger:
    def __init__(self, first_name, last_name, flight_number, seat_number=None):
        # Inicjalizuje pasażera z imieniem, nazwiskiem, numerem lotu i opcjonalnie numerem miejsca
        self.first_name = first_name
        self.last_name = last_name
        self.flight_number = flight_number
        self.seat_number = seat_number

    # Zmienia numer miejsca pasażera
    def change_seat(self, new_seat):
        self.seat_number = new_seat


    # Zwraca reprezentację tekstową pasażera
    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.flight_number}, {self.seat_number})"