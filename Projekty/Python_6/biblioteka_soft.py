#Biblioteka
print("Witamy w Bibliotece")

lista_ksiag = [
    {
    "tytul": "The Division",
    "autor": "Tom Clancy",
    "rok_wydania": 2017,
    "cena": 19.99,
    "ilosc_na_stanie": 10,
    "kategoria": "thriller",
    "ISBN": "978-3-16-148410-0"
    },
    {
    "tytul": "Śpiączka",
    "autor": "Graham Masterton",
    "rok_wydania": 2015,
    "cena": 39.99,
    "ilosc_na_stanie": 6,
    "kategoria": "horror",
    "ISBN": "978-0-261-10221-7"
    }
]
saldo = 10000
historia = []

while True:
    print("Wybierz jedną z poniższych opcji(Podaj numer):")
    komenda = input("""
        1. doładowanie
        2. wypożycz
        3. zakup
        4. bieżący_stan
        5. zestawienie
        6. szczegóły_książki
        7. dziennik
        8. zakończ
    """)
    match komenda:
        case "1": #Doładowanie
            kwota = float(input("Wprowadź kwotę o jaką chcesz zmienić saldo: "))
            if kwota + saldo <0:
                print("Saldo nie może być ujemne!")
            else:
                saldo += kwota
                print(f"Aktualne saldo to: {saldo:.2f} zł")
            historia.append(f"Zmiana salda o {kwota:.2f} zł. Nowe saldo: {saldo:.2f} zł")

        case "2": #Wypożyczenie
            tytul = input("Podaj tytuł książki do wypożyczenia: ").lower().strip() #Pobranie tytułu
            ksiazka_znaleziona = False #Flaga informujaca czy ksiazka zostala znaleziona
            for ksiazka in lista_ksiag: #Przeszukiwanie listy ksiag przez pętle "for"
                if ksiazka.get("tytul").lower() == tytul: #sprawdzenie poprawnosci ksiazki po tytule
                    ksiazka_znaleziona = True #Jeśli znaleziono, możemy iść dalej.
                    if ksiazka["ilosc_na_stanie"] <= 0: #Jeśli brak na stanie, dostaniemy info!
                        print("Brak dostępnej książki!")
                        break
                    ksiazka["ilosc_na_stanie"] -= 1 #odjęcie książki ze stanu magazynowego
                    saldo += 12.99  # koszt wypożyczenia książki
                    historia.append(f"Wypożyczenie książki: {ksiazka['tytul']}, {ksiazka['autor']}, 1 sztuka")
                    print(f"\nWypożyczono książkę: \"{ksiazka['tytul']}\"") #informacja dla użytkownika o wypożyczeniu
                    print(f"Koszt wypożyczenia: 12.99 zł")
                    print(f"Ilość egzemplarzy na stanie: {ksiazka['ilosc_na_stanie']}")
                    print(f"Nowe saldo: {saldo:.2f} zł\n (Zaaktualizowane)")
                    break
            if not ksiazka_znaleziona: #Jeśli nie ma takiej ksiązki w bazie danych, dostajemy info!
                print("Nie ma takiej książki.")

        case "3": #Zakup nowej książki
            tytul = input("Podaj tytuł książki: ") # Pobieranie wszystkich danych o książce od użytkownika
            autor = input("Podaj autora książki: ")
            koszt = float(input("Podaj koszt zakupu książki: "))
            ilosc = int(input("Podaj ilość egzemplarzy: "))
            kategoria = input("Podaj kategorie książki: ")
            numer_isbn = input("Podaj numer ISBN książki: ")
            rok_wydania = int(input("Podaj rok wydania książki: "))
            if saldo - (koszt * ilosc) < 0: # Sprawdzenie czy mamy wystarczające saldo, by kupić wszystkie egzemplarze
                print("Saldo nie może być ujemne!")
                historia.append( #Dodajemy do historii info
                    f"Próba zakupu książki: {tytul}, {koszt}, {ilosc} sztuk - nieudana"
                )
                continue
            else: #Jeśli saldo wystarczy – odejmujemy koszt całkowity zakupu od salda
                saldo -= koszt * ilosc
                znaleziono_ksiazke = False #Flaga, czy książka istnieje w bazie?
                for ksiazka in lista_ksiag: #Sprawdzamy, czy książka już jest w bibliotece (po numerze ISBN)
                    if ksiazka.get("ISBN") == numer_isbn:
                        znaleziono_ksiazke = True #Flaga, że książka już istnieje
                        ksiazka["ilosc_na_stanie"] += ilosc #Dodanie książki do stanu magazynowego
                        break
                if not znaleziono_ksiazke: #Jeśli książki jeszcze nie ma w bibliotece, dodajemy ją jako nową pozycję.
                    lista_ksiag.append(
                        {
                            "tytul": tytul,
                            "autor": autor,
                            "cena": koszt,
                            "ilosc_na_stanie": ilosc,
                            "ilosc": ilosc,
                            "kategoria": kategoria,
                            "ISBN": numer_isbn,
                            "rok_wydania": rok_wydania,
                        }
                    )
                    historia.append(f"Zakup książki: {tytul}, {koszt}, {ilosc} sztuk")
                    #Dodajemy do historii, zakup nowej książki w tym wypadku
        case "4": #Sprawdzanie stanu konta biblioteki
            print(f"Stan konta biblioteki to: {saldo:.2f} zł") #Sprawdź aktualny stan finansowy

        case "5": #Zestawienie
            print("Aktualne zestawienie: ") #Wydrukowanie zestawienia
            wartosc_zbioru = 0 #Wartość początkowa
            for ksiazka in lista_ksiag: #Przeszukanie po liście książek
                wartosc = ksiazka["cena"] * ksiazka["ilosc_na_stanie"] #Wartość wszystkich książek i ilosc na stanie
                wartosc_zbioru += wartosc #dodanie wartosci książek do podsumowania wartosci ksiag
                print(f"{ksiazka['tytul']} – {ksiazka['autor']} – {ksiazka['ilosc_na_stanie']} szt. – {ksiazka['cena']} zł/szt. – Wartość: {wartosc:.2f} zł")
            #Printowanie danych do zestawienia
            print(f"Łączna wartość ksiąg: {wartosc_zbioru:.2f} zł")
            print(f"Aktualne saldo biblioteki to: {saldo:.2f} zł")

        case "6": #Szczegóły książki
            isbn = input("Wprowadź numer ISBN aby wyświetlić: ") #Input na ISBN
            ksiazka_znaleziona = False #Flaga, gdy książka nie zostanie znaleziona,
            for ksiazka in lista_ksiag: #Przeszukanie listy ksiąg
                if ksiazka["ISBN"] == isbn: #Warunek, jeśli książka posiada numer ISBN podany wyżej
                    ksiazka_znaleziona = True #Printowanie danych o książce
                    print("\nSzczegóły książki:")
                    print(f"Tytuł: {ksiazka['tytul']}")
                    print(f"Autor: {ksiazka['autor']}")
                    print(f"Rok wydania: {ksiazka['rok_wydania']}")
                    print(f"Kategoria: {ksiazka['kategoria']}")
                    print(f"Cena: {ksiazka['cena']} zł")
                    print(f"Ilość na stanie: {ksiazka['ilosc_na_stanie']}")
                    print(f"ISBN: {ksiazka['ISBN']}\n")
                    break
            if not ksiazka_znaleziona: #Warunek nie spełniony + print
                print("Nie znaleziono!")

        # case "7": #Dziennik działań
        #     od = input("Podaj wartość 'od' (numer transakcji): ")
        #     do = input("Podaj wartość 'do' (numer transakcji): ")
        #     if od:
        #         od = int(od)
        #     else:
        #         od = 0
        #     if do:
        #         do = int(do)
        #     else:
        #         do = len(historia)
        #         print(historia[od:do])
        case "7":
            if not historia:
                print("Brak zapisanych operacji w dzienniku.")
            else:
                print("\nHistoria operacji:")
                for wpis in historia:
                    print(f"- {wpis}")
            print()

        case "8":
            print("Zakończono działanie programu.")
            break
# if komenda in ("8", "zakoncz", "zakończ"):
#     print("Zakończono działanie programu.")
#     break


