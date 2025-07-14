class Steward:
    def __init__(self, first_name, last_name, flight_number):
        # Inicjalizuje stewarda/stewardessę z imieniem, nazwiskiem i przypisanym numerem lotu
        self.first_name = first_name
        self.last_name = last_name
        self.flight_number = flight_number

    # Zwraca reprezentację tekstową stewarda/stewardessy
    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.flight_number})"