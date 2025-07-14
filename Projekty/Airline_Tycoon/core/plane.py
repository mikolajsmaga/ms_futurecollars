class Plane:
    def __init__(self, model, capacity, km_range):
        # Inicjalizuje samolot z modelem, pojemnością (ilością miejsc) i zasięgiem (w kilometrach)
        self.model = model
        self.capacity = capacity
        self.km_range = km_range
        self.route = None
        self.is_available = True #Dostępny

    def assign_route(self, route_name, distance):
        # Przypisuje trasę, jeśli dystans nie przekracza zasięgu samolotu
        if distance > self.km_range:
            print(f"Trasa {route_name} ({distance} km) jest zbyt długa dla samolotu {self.model}.")
            return False

        self.route = {"name": route_name, "distance": distance}
        print(f"Samolot {self.model} przypisany do trasy {route_name} ({distance} km).")
        return True

    # Zwraca reprezentację tekstową samolotu
    def __repr__(self):
        status = "✅ Dostępny" if self.is_available else "❌ Niedostępny"
        return f"{self.model} - Pojemność: {self.capacity}, Zasięg: {self.km_range}km. [{status}]"

