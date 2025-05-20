#BAZA SZKOLNA

print("Witamy w szkolnej bazie, co chcesz zrobić?")
print("1. Utwórz (Nowy użytkownik)")
print("2. Zarządzanie użytkownikiem")
print("3. Zakończ")

input("Wybierz opcję (1-3): ")

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa
    def __str__(self):
        return f"{self.imie} {self.nazwisko} z klasy {self.klasa}"
    def __repr__(self):
        return f"Uczen(imie = '{self.imie}', nazwisko = '{self.nazwisko}', klasa = '{self.klasa}')"

class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy = klasy #Lista klas
    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.przedmiot} w klasach {self.klasy}"
    def __repr__(self):
        return f"Nauczyciel(imie = '{self.imie}', nazwisko = '{self.nazwisko}', przedmiot = '{self.przedmiot}', klasy = '{self.klasy}')"

class Wychowawca:
    def __init__(self, imie, nazwisko, klasa_przypisana):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa_przypisana = klasa_przypisana
    def __str__(self):
        return f"{self.imie} {self.nazwisko} wychowawca klasy {self.klasa_przypisana}"
    def __repr__(self):
        return f"Wychowawca(imie = '{self.imie}', nazwisko = '{self.nazwisko}', klasa_przypisana = '{self.klasa_przypisana}')"

