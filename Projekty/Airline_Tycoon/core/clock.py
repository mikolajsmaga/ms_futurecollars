import datetime
import random

class GameClock:
    def __init__(self, airport, event_manager):
        self.current_time = datetime.datetime(2025, 1, 1, 8, 0)  # Start: 1 stycznia 2025, godz. 8:00
        self.airport = airport
        self.event_manager = event_manager
        self.tick_interval = datetime.timedelta(minutes=10)  # Każdy krok to 10 minut

    def tick(self):
        # Przesuwamy zegar o 10 minut
        self.current_time += self.tick_interval
        print(f"\n🕓 Aktualny czas symulacji: {self.current_time.strftime('%Y-%m-%d %H:%M')}")

        # Losowe zdarzenia mogą wystąpić z prawdopodobieństwem 15%
        if random.random() < 0.15:
            self.event_manager.trigger_random_event()