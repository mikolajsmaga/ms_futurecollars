import random
import time

class EventManager:
    def __init__(self, airport):
        self.airport = airport

    def trigger_random_event(self):
        events = [
            self.flight_delay,
            self.steward_absence,
            self.plane_breakdown,
            self.overbooking_issue,
            self.weather_warning,
            self.airport_strike,
            self.fuel_price_spike,
            self.security_alert
        ]
        random.choice(events)()

    def flight_delay(self):
        if self.airport.flights:
            flight = random.choice(self.airport.flights)
            delay_time = random.randint(15, 120)
            print(f"🕒 Lot {flight.flight_number} został opóźniony o {delay_time} minut z powodu warunków pogodowych.")

    def steward_absence(self):
        if self.airport.stewards:
            steward = random.choice(self.airport.stewards)
            print(
                f"⚠️ Steward {steward.first_name} {steward.last_name} nie pojawił się do pracy. Lot może być zagrożony!")

    def plane_breakdown(self):
        if self.airport.airplanes:
            plane = random.choice(self.airport.airplanes)
            issue = random.choice([
                "usterka silnika",
                "problem z elektroniką pokładową",
                "przeciek w zbiorniku paliwa",
                "usterka hydrauliczna",
                "usterka systemu nawigacyjnego"
            ])
            repair_time = random.randint(1, 3)  # godziny
            print(f"🔧 Samolot {plane.model} ma problem: {issue}. Szacowany czas naprawy: {repair_time}h.")
            plane.is_available = False  # Możesz dodać takie pole do klasy Plane

    def overbooking_issue(self):
        # Zdarzenie: zbyt wielu pasażerów przypisanych do jednego lotu
        for flight in self.airport.flights:
            if flight.plane and len(flight.passengers) > flight.plane.capacity:
                print(
                    f"🚨 PRZEPEŁNIENIE! Lot {flight.flight_number} ma więcej pasażerów ({len(flight.passengers)}) niż miejsc ({flight.plane.capacity}).")

    def security_alert(self):
        # Zdarzenie: alert bezpieczeństwa
        print("🔒 ALERT BEZPIECZEŃSTWA! Tymczasowo zaostrzono kontrolę na lotnisku.")
        for flight in self.airport.flights:
            print(f"🛂 Lot {flight.flight_number} będzie miał opóźnienie z powodu dodatkowej kontroli bezpieczeństwa.")

    def fuel_price_spike(self):
        # Zdarzenie: gwałtowny wzrost cen paliwa
        increase = random.randint(10, 40)  # Wzrost procentowy
        print(f"⛽ Ceny paliwa wzrosły o {increase}%. Koszty operacyjne linii lotniczych idą w górę!")

    def airport_strike(self):
        # Zdarzenie: strajk personelu lotniska
        print("🚧 STRAJK! Personel lotniska przerywa pracę. Wszystkie loty są zawieszone na czas nieokreślony.")

    def weather_warning(self):
        # Zdarzenie: ostrzeżenie meteorologiczne wpływające na wszystkie loty
        print("🌪️ ALERT METEO: Pogarszające się warunki pogodowe mogą opóźnić wszystkie loty!")
        for flight in self.airport.flights:
            print(f"⚠️ Lot {flight.flight_number} może zostać opóźniony lub odwołany.")
