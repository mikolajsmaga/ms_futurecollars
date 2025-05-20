#BAZA SZKOLNA

print("Witamy w szkolnej bazie, co chcesz zrobić?")
print("1. Utwórz (Nowy użytkownik)")
print("2. Zarządzanie użytkownikiem")
print("3. Zakończ")
wariant = input("Wybierz opcję (1-3): ")
#Klasy użytkowników
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
#Listy użytkowników
uczniowie = []
nauczyciele = []
wychowawcy = []
#Funkcja tworzenia nowego użytkownika
def nowy_uzytkownik(): #Utwórz
    while True:
        print("Stwórz nowego użytkownika: \n")
        print("1. Uczeń")
        print("2. Nauczyciel")
        print("3. Wychowawca")
        print("4. Koniec")
        opcja = input("Wybierz opcję (1-4): ").strip().lower()
        if opcja in ["1", "uczen", "uczeń", "Uczen", "Uczeń"]: #UCZEŃ
            imie = input("Podaj imię ucznia: ").strip()
            nazwisko = input("Podaj nazwisko ucznia: ").strip()
            klasa = input("Podaj klasę ucznia: ").strip().upper()

            uczniowie.append(Uczen(imie, nazwisko, klasa))
            print(f"Uczeń {imie} {nazwisko }został dodany do klasy {klasa}.")

        elif opcja in ["2", "nauczyciel", "Nauczyciel"]: #NAUCZYCIEL
            imie = input("Podaj imię nauczyciela: ")
            nazwisko = input("Podaj nazwisko nauczyciela: ")
            przedmiot = input("Podaj przedmiot nauczania: ")

            klasy = [] #OPCJA W JAKIEJ KLASIE NAUCZANIE
            print(f"Podaj klasy w których będzie nauczanie przedmiotu {przedmiot}: ")
            while True:
                klasa = input("Podaj klasę: ").strip().upper()
                if klasa == "":
                    break
                klasy.append(klasa)
                # Tworzymy obiekt nauczyciela i dodajemy do listy
            nauczyciele.append(Nauczyciel(imie, nazwisko, przedmiot, klasy))
            print(f"Nauczyciel {imie} {nazwisko} dodany do przedmiotu {przedmiot}.")

        elif opcja in ["3", "wychowawca", "Wychowawca"]: #WYCHOWAWCA
            imie = input("Podaj imie wychowawcy: ")
            nazwisko = input("Podaj nazwisko wychowawcy: ")
            klasa = input("Podaj klasę której będziesz wychowawcą: ")
            # Tworzymy obiekt wychowawcy i dodajemy do listy
            wychowawcy.append(Wychowawca(imie, nazwisko, klasa))
            print(f"Wychowawcą klasy {klasa} jest {imie} {nazwisko}.")

        elif opcja in ["4", "koniec"]: #ZAKAŃCZAMY I WRACAMY DO MENU
            print("Powrót do głównego menu.")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

def zarzadzaj_uzytkownikiem(): #Zarządzaj
    pass