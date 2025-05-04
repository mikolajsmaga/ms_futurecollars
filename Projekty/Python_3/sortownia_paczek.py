"""
Sortownia Paczek
Napisz program do obsługi ładowarki paczek. Po uruchomieniu, aplikacja pyta ile paczek chcesz wysłać,
a następnie wymaga podania wagi dla każdej z nich.

Na koniec działania program powinien wyświetlić w podsumowaniu:
#Podsumowanie
Liczbę paczek wysłanych
Liczbę kilogramów wysłanych
Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik

Restrykcje:

Waga elementów musi być z przedziału od 1 do 10 kg.
Każda paczka może maksymalnie zmieścić 20 kilogramów towaru.
W przypadku, jeżeli dodawany element przekroczy wagę towaru, ma zostać dodany do nowej paczki, a obecna wysłana.
W przypadku podania wagi elementu mniejszej od 1kg lub większej od 10kg,
dodawanie paczek zostaje zakończone i wszystkie paczki są wysłane. Wyświetlane jest podsumowanie.
"""

#def sortownia_paczek():
max_waga_paczki = 20  # Maksymalna waga paczki
ilosc_paczek = []     # Lista wysłanych paczek
aktualna_paczka = []  # Bieżąca pakowana paczka
waga_paczek = 0       # Łączna masa wszystkich przedmiotów

# Pytanie o ilość przedmiotów do spakowania
ilosc_przedmiotow = int(input("Ile chcesz wysłać paczek/przedmiotów?: "))

# Pętla – użytkownik wpisuje wagę każdego przedmiotu
for i in range(ilosc_przedmiotow):
    waga = float(input(f"Podaj wagę przedmiotu {i+1} (1-10 kg): "))

    # Sprawdzenie, czy waga jest w dopuszczalnym zakresie
    if waga < 1 or waga > 10:
        print("Waga jest nieprawidłowa! Zakańczam operację, paczki zostały wysłane.")
        if aktualna_paczka:
            ilosc_paczek.append(aktualna_paczka)  # Dodaj aktualną paczkę, jeśli coś w niej było
        break # Przerywamy dalsze dodawanie paczek

    # Sprawdzenie, czy przedmiot zmieści się w bieżącej paczce
    if sum(aktualna_paczka) + waga > max_waga_paczki:
        ilosc_paczek.append(aktualna_paczka)      # Zapisz pełną paczkę
        aktualna_paczka = [waga]                  # Rozpocznij nową paczkę z tym przedmiotem
    else:
        aktualna_paczka.append(waga)              # Dodaj przedmiot do bieżącej paczki

    waga_paczek += waga  # Dodaj wagę przedmiotu do całkowitej sumy

# Dodanie ostatniej paczki po zakończeniu pętli
if aktualna_paczka:
    ilosc_paczek.append(aktualna_paczka)

# Obliczenie pustej przestrzeni (straty)
suma_pustych = len(ilosc_paczek) * max_waga_paczki - waga_paczek

# Znalezienie paczki z największą ilością pustych kg
najwiecej_pustych = max_waga_paczki - sum(ilosc_paczek[0])
nr_paczki = 1

for idx, paczka in enumerate(ilosc_paczek):
    puste = max_waga_paczki - sum(paczka)
    if puste > najwiecej_pustych:
        najwiecej_pustych = puste
        nr_paczki = idx + 1  # +1 bo numerujemy od 1

#musiałem sprawdzić co to ten idx, indeks i pomógł dodatkowo w temacie

# =====================
# PODSUMOWANIE
# =====================
print("\n--- PODSUMOWANIE ---")
print(f"Liczba paczek wysłanych: {len(ilosc_paczek)}")
print(f"Liczba kilogramów wysłanych: {waga_paczek} kg")
if suma_pustych > 0:
    print(f"Suma pustych kilogramów: {suma_pustych} kg")
    print(f"Paczka z największą ilością pustych kg: #{nr_paczki} ({najwiecej_pustych} kg pustych)")
else:
    print("Brak pustych kilogramów – pakowanie było idealne!")

