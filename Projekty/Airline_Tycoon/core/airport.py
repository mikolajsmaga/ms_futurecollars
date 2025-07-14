from .passenger import Passenger
from .airline import Airline
from .steward import Steward

class Airport:
    def __init__(self):
        self.passengers = []
        self.airlines = []
        self.stewards = []
        self.terminals = []
        self.gates = []
        self.flights = []
        self.airplanes = []

    # Add a new passenger to the airport
    def add_passenger(self, passenger: Passenger):
        self.passengers.append(passenger)

    # Add a new airline to the airport
    def add_airline(self, airline: Airline):
        self.airlines.append(airline)

    # Add a new steward to the airport
    def add_steward(self, steward: Steward):
        self.stewards.append(steward)

    # Find passenger by first and last name
    def find_passenger(self, first_name: str, last_name: str) -> Passenger | None:
        # Iterate over passengers to find a match
        for person in self.passengers:
            if person.first_name == first_name and person.last_name == last_name:
                return person
        return None

    # Find airline by name
    def find_airline(self, name: str) -> Airline | None:
        # Iterate over airlines to find a match
        for airline in self.airlines:
            if airline.name == name:
                return airline
        return None

    # Find steward by first and last name
    def find_steward(self, first_name: str, last_name: str) -> Steward | None:
        # Iterate over stewards to find a match
        for person in self.stewards:
            if person.first_name == first_name and person.last_name == last_name:
                return person
        return None

    # Remove passenger by object reference
    def remove_passenger(self, passenger: Passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)

    # Remove airline by object reference
    def remove_airline(self, airline: Airline):
        if airline in self.airlines:
            self.airlines.remove(airline)

    # Remove steward by object reference
    def remove_steward(self, steward: Steward):
        if steward in self.stewards:
            self.stewards.remove(steward)