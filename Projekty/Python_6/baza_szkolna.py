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
#klasy = []
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

def zarzadzaj_uzytkownikiem():
    while True:
        wybor = input("\nWybierz opcję: uczeń / nauczyciel / wychowawca / klasa / koniec: ").strip().lower()

        match wybor:
            case "uczeń" | "uczen":
                imie = input("Podaj imię ucznia: ").strip()
                nazwisko = input("Podaj nazwisko ucznia: ").strip()
                info_ucznia(imie, nazwisko)

            case "nauczyciel":
                imie = input("Podaj imię nauczyciela: ").strip()
                nazwisko = input("Podaj nazwisko nauczyciela: ").strip()
                info_nauczyciela(imie, nazwisko)

            case "wychowawca":
                imie = input("Podaj imię wychowawcy: ").strip()
                nazwisko = input("Podaj nazwisko wychowawcy: ").strip()
                info_wychowawcy(imie, nazwisko)

            case "klasa":
                klasa = input("Podaj nazwę klasy (np. 3C): ").strip().upper()
                info_klas(klasa)

            case "koniec":
                print("Powrót do menu głównego.")
                break


def info_ucznia(imie, nazwisko): #Zapytanie o imię i nazwisko #or info_ucznia(imie, nazwisko)

    uczen_znaleziony = None #Przeszukanie ucznia w liście uczniów przez pętle for
    for uczen in uczniowie:
        if uczen.imie.lower() == imie.lower() and uczen.nazwisko.lower() == nazwisko.lower():
            uczen_znaleziony = uczen
            break
    if not uczen_znaleziony: #Warunek gdy nie został znaleziony uczeń
        print("Nie ma takiego ucznia!")
        return

    print(f"\nUczeń: {uczen_znaleziony.imie} {uczen_znaleziony.nazwisko}, Klasa: {uczen_znaleziony.klasa}")
    print("Przedmioty i nauczyciele:")

    znaleziono_lekcje = False
    for nauczyciel in nauczyciele:
        if uczen_znaleziony.klasa in nauczyciel.klasy:
            print(f"- {nauczyciel.przedmiot} prowadzi {nauczyciel.imie} {nauczyciel.nazwisko}")
            znaleziono_lekcje = True

    if not znaleziono_lekcje:
        print("Brak przypisanych przedmiotów lub nauczycieli dla tej klasy.")

def info_nauczyciela(imie, nazwisko):
    nauczyciel_znaleziony = None
    for nauczyciel in nauczyciele:
        if nauczyciel.imie.lower()== imie.lower() and nauczyciel.nazwisko.lower() == nazwisko.lower():
            nauczyciel_znaleziony = nauczyciel
            break

    # Jeśli nauczyciel nie został znaleziony – komunikat i zakończenie funkcji
    if not nauczyciel_znaleziony:
        print("Nie znaleziono takiego nauczyciela!")
        return

        # Wyświetlenie informacji o nauczycielu
    print(f"\nNauczyciel: {nauczyciel_znaleziony.imie} {nauczyciel_znaleziony.nazwisko}")
    print(f"Przedmiot: {nauczyciel_znaleziony.przedmiot}")
    print("Prowadzi zajęcia w klasach:")

    # Wypisanie wszystkich klas przypisanych temu nauczycielowi
    for klasa in nauczyciel_znaleziony.klasy:
        print(f"- Klasa {klasa}")

def info_wychowawcy(imie, nazwisko):
    for wych in wychowawcy:
        if wych.imie.lower() == imie.lower() and wych.nazwisko.lower() == nazwisko.lower():
            print(f"{wych.imie} {wych.nazwisko} jest wychowawcą klasy {wych.klasa_przypisana}")
            return
    print("Nie znaleziono wychowawcy.")

def info_klas(klasa):
    klasa = klasa.upper()  # Upewniamy się, że porównujemy w jednolitym formacie

    # Szukamy wychowawcy tej klasy
    wychowawca_klasy = None
    for wychowawca in wychowawcy:
        if wychowawca.klasa_przypisana.upper() == klasa:
            wychowawca_klasy = wychowawca
            break

    # Szukamy uczniów tej klasy
    uczniowie_klasy = []
    for uczen in uczniowie:
        if uczen.klasa.upper() == klasa:
            uczniowie_klasy.append(uczen)

    # Szukamy nauczycieli uczących w tej klasie
    nauczyciele_klasy = []
    for nauczyciel in nauczyciele:
        if klasa in nauczyciel.klasy:
            nauczyciele_klasy.append(nauczyciel)

    # Wyświetlamy dane klasy
    print(f"\nInformacje o klasie {klasa}:")

    if wychowawca_klasy:
        print(f"- Wychowawca: {wychowawca_klasy.imie} {wychowawca_klasy.nazwisko}")
    else:
        print("- Brak przypisanego wychowawcy.")

    if uczniowie_klasy:
        print("- Uczniowie:")
        for uczen in uczniowie_klasy:
            print(f"  • {uczen.imie} {uczen.nazwisko}")
    else:
        print("- Brak uczniów w tej klasie.")

    if nauczyciele_klasy:
        print("- Nauczyciele:")
        for nauczyciel in nauczyciele_klasy:
            print(f"  • {nauczyciel.imie} {nauczyciel.nazwisko} – {nauczyciel.przedmiot}")
    else:
        print("- Brak przypisanych nauczycieli.")

