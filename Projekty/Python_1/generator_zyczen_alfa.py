#Powitanie użytkownika
#from Projekty.Python_1.generator_zyczen import rok_urodzenia

import datetime


print("Witaj w generatorze życzeń urodzinowych!")

# Pytanie do użytkownika o kategorię (bez sprawdzania)
kategoria = input("Podaj kategorię (na razie dostępne tylko: urodziny): ").lower().strip()

# Od razu pytamy o resztę danych
imie_odbiorcy = input("Podaj imię odbiorcy: ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))
twoja_wiadomosc = input("Wpisz swój tekst: ")
imie_adresata = input("Podaj swoje imię: ")

# Obliczanie wieku
aktualny_rok = datetime.datetime.now().year
wiek = aktualny_rok - rok_urodzenia

# Generowanie kartki
print("\n🎂 Twoja kartka urodzinowa 🎂")
print("-" * 40)
print(f"{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek} urodzin!")
print()
print(twoja_wiadomosc)
print()
print(f"Pozdrawia: {imie_adresata}")
print("-" * 40)







