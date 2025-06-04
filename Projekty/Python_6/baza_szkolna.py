# ─────────────────────────────────────────────────────────────────────
# BAZA SZKOLNA – SYSTEM ZARZĄDZANIA UCZNIAMI, NAUCZYCIELAMI I KLASAMI
# Autor: [Mikołaj] | Data: [04.06.2025]
# ─────────────────────────────────────────────────────────────────────
# Klasy użytkowników
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
        self.klasy = klasy  # Lista klas

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


# Listy użytkowników
uczniowie = []
nauczyciele = []
wychowawcy = []


# klasy = []
# Funkcja tworzenia nowego użytkownika

def dodaj_ucznia():
    imie = input("Podaj imię ucznia: ").strip()
    nazwisko = input("Podaj nazwisko ucznia: ").strip()
    klasa = input("Podaj klasę ucznia: ").strip().upper()

    uczniowie.append(Uczen(imie, nazwisko, klasa))
    print(f"Uczeń {imie} {nazwisko} został dodany do klasy {klasa}.")
    for uczen in uczniowie:
        if uczen.imie.lower() == imie.lower() and uczen.nazwisko.lower() == nazwisko.lower() and uczen.klasa.upper() == klasa:
            print("Uczeń już istnieje w bazie.")
            return

def dodaj_nauczyciela():
    imie = input("Podaj imię nauczyciela: ").strip()
    nazwisko = input("Podaj nazwisko nauczyciela: ").strip()
    przedmiot = input("Podaj przedmiot nauczania: ").strip()

    klasy = []
    print(f"Podaj klasy, w których {imie} {nazwisko} będzie uczyć przedmiotu {przedmiot}:")
    while True:
        klasa = input("Podaj klasę (Enter by zakończyć): ").strip().upper()
        if not klasa:
            break
        klasy.append(klasa)

    nauczyciele.append(Nauczyciel(imie, nazwisko, przedmiot, klasy))
    print(f"Nauczyciel {imie} {nazwisko} został dodany.")

def dodaj_wychowawce():
    imie = input("Podaj imię wychowawcy: ").strip()
    nazwisko = input("Podaj nazwisko wychowawcy: ").strip()
    klasa = input("Podaj klasę, której będzie wychowawcą: ").strip().upper()

    wychowawcy.append(Wychowawca(imie, nazwisko, klasa))
    print(f"Wychowawcą klasy {klasa} został {imie} {nazwisko}.")

def nowy_uzytkownik():  # Utwórz
    while True:
        print("\nStwórz nowego użytkownika:")
        print("1. Uczeń")
        print("2. Nauczyciel")
        print("3. Wychowawca")
        print("4. Powrót")

        opcja = input("Wybierz opcję (1-4): ").strip().lower()

        if opcja in ("1", "uczen", "uczeń"):
            dodaj_ucznia()
        elif opcja in ("2", "nauczyciel"):
            dodaj_nauczyciela()
        elif opcja in ("3", "wychowawca"):
            dodaj_wychowawce()
        elif opcja in ("4", "koniec", "powrót", "powrot"):
            print("Powrót do menu głównego.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def zarzadzaj_uzytkownikiem():
    while True:
        print("\nZarządzanie użytkownikami — wybierz opcję:")
        print("1. Uczeń")
        print("2. Nauczyciel")
        print("3. Wychowawca")
        print("4. Klasa")
        print("5. Koniec")

        wybor = input("Twój wybór (1–5 lub wpisz nazwę): ").strip().lower()

        match wybor:
            case "1" | "uczeń" | "uczen":
                imie = input("Podaj imię ucznia: ").strip()
                nazwisko = input("Podaj nazwisko ucznia: ").strip()
                info_ucznia(imie, nazwisko)

            case "2" | "nauczyciel":
                imie = input("Podaj imię nauczyciela: ").strip()
                nazwisko = input("Podaj nazwisko nauczyciela: ").strip()
                info_nauczyciela(imie, nazwisko)

            case "3" | "wychowawca":
                imie = input("Podaj imię wychowawcy: ").strip()
                nazwisko = input("Podaj nazwisko wychowawcy: ").strip()
                info_wychowawcy(imie, nazwisko)

            case "4" | "klasa":
                klasa = input("Podaj nazwę klasy (np. 3C): ").strip().upper()
                wyswietl_info_o_klasie(klasa)

            case "5" | "koniec":
                print("Powrót do menu głównego.")
                break


def info_ucznia(
    imie, nazwisko
):  # Zapytanie o imię i nazwisko #or info_ucznia(imie, nazwisko)
    uczen_znaleziony = None  # Przeszukanie ucznia w liście uczniów przez pętle for
    for uczen in uczniowie:
        if (
            uczen.imie.lower() == imie.lower()
            and uczen.nazwisko.lower() == nazwisko.lower()
        ):
            uczen_znaleziony = uczen
            break
    if not uczen_znaleziony:  # Warunek gdy nie został znaleziony uczeń
        print("Nie ma takiego ucznia!")
        return

    print(
        f"\nUczeń: {uczen_znaleziony.imie} {uczen_znaleziony.nazwisko}, Klasa: {uczen_znaleziony.klasa}"
    )
    print("Przedmioty i nauczyciele:")

    znaleziono_lekcje = False
    for nauczyciel in nauczyciele:
        if uczen_znaleziony.klasa in nauczyciel.klasy:
            print(
                f"- {nauczyciel.przedmiot} prowadzi {nauczyciel.imie} {nauczyciel.nazwisko}"
            )
            znaleziono_lekcje = True

    if not znaleziono_lekcje:
        print("Brak przypisanych przedmiotów lub nauczycieli dla tej klasy.")


def info_nauczyciela(imie, nazwisko):
    nauczyciel_znaleziony = None
    for nauczyciel in nauczyciele:
        if (
            nauczyciel.imie.lower() == imie.lower()
            and nauczyciel.nazwisko.lower() == nazwisko.lower()
        ):
            nauczyciel_znaleziony = nauczyciel
            break

    # Jeśli nauczyciel nie został znaleziony – komunikat i zakończenie funkcji
    if not nauczyciel_znaleziony:
        print("Nie znaleziono takiego nauczyciela!")
        return

        # Wyświetlenie informacji o nauczycielu
    print(
        f"\nNauczyciel: {nauczyciel_znaleziony.imie} {nauczyciel_znaleziony.nazwisko}"
    )
    print(f"Przedmiot: {nauczyciel_znaleziony.przedmiot}")
    print("Prowadzi zajęcia w klasach:")

    # Wypisanie wszystkich klas przypisanych temu nauczycielowi
    for klasa in nauczyciel_znaleziony.klasy:
        print(f"- Klasa {klasa}")

def info_wychowawcy(imie, nazwisko):
    for wych in wychowawcy:
        if (
            wych.imie.lower() == imie.lower()
            and wych.nazwisko.lower() == nazwisko.lower()
        ):
            print(
                f"{wych.imie} {wych.nazwisko} jest wychowawcą klasy {wych.klasa_przypisana}"
            )
            return
    print("Nie znaleziono wychowawcy.")

def znajdz_wychowawce_dla_klasy(nazwa_klasy):
    for wychowawca in wychowawcy:
        if wychowawca.klasa_przypisana.upper() == nazwa_klasy:
            return wychowawca
    return None

def znajdz_uczniow_z_klasy(nazwa_klasy):
    return [uczen for uczen in uczniowie if uczen.klasa.upper() == nazwa_klasy]

def znajdz_nauczycieli_dla_klasy(nazwa_klasy):
    return [nauczyciel for nauczyciel in nauczyciele if nazwa_klasy in nauczyciel.klasy]

def wyswietl_info_o_klasie(klasa):
    klasa = klasa.upper()

    wychowawca = znajdz_wychowawce_dla_klasy(klasa)
    uczniowie_klasy = znajdz_uczniow_z_klasy(klasa)
    nauczyciele_klasy = znajdz_nauczycieli_dla_klasy(klasa)

    print(f"\nInformacje o klasie {klasa}:")

    if wychowawca:
        print(f"- Wychowawca: {wychowawca.imie} {wychowawca.nazwisko}")
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

def menu_glowne():
    while True:
        print("\n--- MENU GŁÓWNE ---")
        print("1. Dodaj użytkownika")
        print("2. Zarządzaj użytkownikiem")
        print("3. Zakończ")

        wybor = input("Wybierz opcję (1–3): ").strip()

        if wybor == "1":
            nowy_uzytkownik()
        elif wybor == "2":
            zarzadzaj_uzytkownikiem()
        elif wybor == "3":
            print("Zakończono program.")
            break
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    menu_glowne()