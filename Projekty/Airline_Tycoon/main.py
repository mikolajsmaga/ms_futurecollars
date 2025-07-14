from core.passenger import Passenger
from core.steward import Steward
from core.airline import Airline
from core.flight import Flight
from core.plane import Plane
from core.airport import Airport
from core.route import Route
from core.event import EventManager
from core.clock import GameClock
from core.interface import MainMenu
import time

def setup_game():
    # Tworzymy lotnisko
    airport = Airport()

    # Tworzymy linię lotniczą
    airline_company = Airline("LOT Polish Airlines")
    airport.add_airline(airline_company)

    # Tworzymy samolot i dodajemy do lotniska
    boeing = Plane("Boeing 737", 180, 3000)
    airport.airplanes.append(boeing)

    # Tworzymy lot
    flight1 = Flight("LO123", airline_company)
    airline_company.add_flight(flight1)
    airport.flights.append(flight1)

    # Przypisujemy samolot do lotu
    flight1.assign_plane(boeing)

    # Tworzymy trasę
    warsaw_berlin = Route("Warszawa", "Berlin", 570)

    # Sprawdzamy czy samolot może obsłużyć trasę
    if warsaw_berlin.can_plane_serve(boeing):
        flight1.route = warsaw_berlin
    else:
        print("Ten samolot nie może obsłużyć tej trasy.")

    # Tworzymy pasażerów
    p1 = Passenger("Jan", "Kowalski", "LO123", "12A")
    p2 = Passenger("Anna", "Nowak", "LO123", "12B")
    flight1.add_passenger(p1)
    flight1.add_passenger(p2)
    airport.add_passenger(p1)
    airport.add_passenger(p2)

    # Tworzymy stewardessę i dodajemy ją do lotniska
    s1 = Steward("Kasia", "Wiśniewska", "LO123")
    airport.add_steward(s1)

    # Inicjalizujemy EventManager i GameClock
    event_manager = EventManager(airport)
    clock = GameClock(airport, event_manager)

    return airport, event_manager, clock

if __name__ == "__main__":
    airport, event_manager, clock = setup_game()

    # Pętla główna symulacji zdarzeń losowych
    for _ in range(10):
        event_manager.trigger_random_event()
        time.sleep(1)

    # Uruchomienie menu
    menu = MainMenu(airport)
    menu.run()