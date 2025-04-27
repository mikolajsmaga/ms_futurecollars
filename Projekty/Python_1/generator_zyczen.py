import datetime

#Powitanie użytkownika
print("Witaj w generatorze życzeń urodzinowych")

#Pytanie do użytkownika o okazję
kategoria = input("Podaj kategorię (na razie dostępne tylko: urodziny): ").strip().lower()
if kategoria != "urodziny":
    print("Inne kategorie są aktualnie niedostępne!")
else:
    imie_odbiorcy = input("Podaj imię odbiorcy: ")
    rok_urodzenia = int(input("Podaj rok urodzenia: "))
    napisz_swoja_wiadomosc = input("Napisz swoją spersonalizowaną wiadomość: ")
    imie_nadawcy = input("Podaj swoje imię (nadawcy): ")

#Obliczanie aktualnego wieku
    aktualny_rok = datetime.datetime.now().year
    wiek = aktualny_rok - rok_urodzenia

# Generowanie kartki
    print("\n🎂 Twoja kartka urodzinowa 🎂")
    print("-" * 40)
    print(f"{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek} urodzin!")
    print()
    print(spersonalizowana_wiadomosc)
    print()
    print(f"Pozdrawia: {imie_nadawcy}")
    print("-" * 40)

