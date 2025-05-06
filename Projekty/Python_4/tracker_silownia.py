"""
Treść zadania

Napisz program śledzący czas ćwiczeń na siłowni.

Działanie programu:

    Program pyta o planowany czas treningu (w minutach). #

    Następnie w pętli pobiera kolejne czasy poszczególnych ćwiczeń (w minutach).

    Każde ćwiczenie musi mieć czas od 5 do 45 minut. #restrakcja #

    Jeśli podany czas jest spoza zakresu, program kończy wprowadzanie. #restrykcja

    Suma czasów ćwiczeń nie może przekroczyć 150% planowanego czasu treningu - jeśli dodanie kolejnego ćwiczenia przekracza ten limit, program kończy wprowadzanie.

    Na koniec program wyświetla:

        Łączny czas ćwiczeń,

        Procent wykorzystania planu,

        Liczbę ćwiczeń trwających dłużej niż 15 minut,

        Najdłuższe pojedyncze ćwiczenie.

Przykłady

Przykład 1:

text
Plan: 60 minut
Czasy: 30, 35, 25 (przekroczenie limitu)

Podsumowanie:
Łączny czas ćwiczeń: 90 minut
Procent wykorzystania planu: 150.00%
Ćwiczenia >15 min: 3
Najdłuższe ćwiczenie: 35 minut
"""
#Tracker Treningowy
czas_treningu = int(input("Podaj ile będziesz czasu trenować? (w minutach): "))
aktualny_czas_treningu = 0
cwiczenia_powyzej_15_minut = 0
najdluzsze_cwiczenie = 0
najkrotsze_cwiczenie = None
liczba_cwiczen = 0
powod_zakonczenia = ""
czasy_cwiczen = []

while True:
    czas_cwiczenia = input(f"Podaj czas cwiczenia {liczba_cwiczen + 1}(w minutach): ")
    if czas_cwiczenia: #!= ""
        czas_cwiczenia = int(czas_cwiczenia)
        if czas_cwiczenia < 5 or czas_cwiczenia > 45:
            #powod_zakonczenia = "Ćwiczenie poza dozwolonym zakresem czasu (5-45 min)."
            break
        if aktualny_czas_treningu + czas_cwiczenia > 1.5 * czas_treningu:
            #powod_zakonczenia = "Przekroczono 150% planowanego czasu treningu – zakończ trening."
            break
        if czas_cwiczenia > 15:
            cwiczenia_powyzej_15_minut += 1
        if najkrotsze_cwiczenie is None or czas_cwiczenia < najkrotsze_cwiczenie:
            najkrotsze_cwiczenie = czas_cwiczenia
        if czas_cwiczenia > najdluzsze_cwiczenie:
            najdluzsze_cwiczenie = czas_cwiczenia
        aktualny_czas_treningu += czas_cwiczenia
        liczba_cwiczen += 1
        czasy_cwiczen.append(czas_cwiczenia)
    else:
        break


print(f"Trening zakończony! Podsumowanie:")
print(f"Liczba wykonanych ćwiczeń: {liczba_cwiczen}")
print(f"Czas trwania treningu: {aktualny_czas_treningu} minut")
print(f"Czas trwania najdłuższego ćwiczenia: {najdluzsze_cwiczenie} minut")
print(f"Wykorzystany czas treningu: {(aktualny_czas_treningu/czas_treningu) * 100}% planu")
print(f"Najkrótszy czas ćwiczenia: {najkrotsze_cwiczenie} minut")
print(f"Liczba ćwiczeń powyżej 15 minut: {cwiczenia_powyzej_15_minut}")
print(f"Zdeklarowany czas treningu to {czas_treningu} minut.")
print(f"Czasy twoich ćwiczeń: {czasy_cwiczen}")
