class Route:
    def __init__(self, from_city, to_city, distance):
        # Tworzy trasę między dwoma miastami z określoną odległością
        self.from_city = from_city
        self.to_city = to_city
        self.distance = distance

    def __repr__(self):
        return f"{self.from_city} → {self.to_city} ({self.distance} km)"

    def can_plane_serve(self, plane):
        # Sprawdza, czy samolot ma wystarczający zasięg
        return plane.km_range >= self.distance