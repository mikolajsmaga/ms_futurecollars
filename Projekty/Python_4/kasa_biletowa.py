"""
Treść zadania
Napisz program do obsługi rezerwacji biletów grupowych na wydarzenie.
Działanie programu:

    Program pyta o liczbę osób w grupie.

    Dla każdej osoby pobiera liczbę biletów, które chce kupić (od 1 do 5).

    Jeśli użytkownik poda wartość spoza zakresu 1–5 lub wprowadzi nieprawidłową wartość, program kończy wprowadzanie danych.

    Na koniec program wyświetla podsumowanie:

        Łączną liczbę biletów,

        Kwotę do zapłaty (20 zł za bilet, zniżka do 15 zł za bilet obowiązuje, jeśli liczba osób w grupie jest co najmniej 5 i łączna liczba biletów wynosi co najmniej 10),

        Największą pojedynczą transakcję biletową,

        Liczbę błędnych wpisów (czyli ile razy wprowadzono nieprawidłową wartość).

Przykłady

Przykład 1:

text
Liczba osób: 5
Bilety: 3, 2, 4, 1, 5

Podsumowanie:
Łączna liczba biletów: 15
Kwota do zapłaty: 225 zł (zniżka)
Największa transakcja: 5
Liczba błędnych wpisów: 0

"""

# Program do zbierania informacji o zakupie biletów w grupie

grupa_osob = int(input("Ile jest osób w grupie? (Podaj liczbę): "))
liczba_biletow_total = 0
najwieksza_ilosc_biletow_w_transakcji = 0
transakcja_z_najwieksza_iloscia = None

for transakcja in range(grupa_osob):
    liczba_biletow_w_transakcji = int(input(f"Podaj liczbę biletów dla osoby {transakcja + 1}: "))

    if liczba_biletow_w_transakcji < 1 or liczba_biletow_w_transakcji > 5:
        print("Nieprawidłowa wartość. Wprowadzanie danych zakończone.")
        break

    liczba_biletow_total += liczba_biletow_w_transakcji

    if liczba_biletow_w_transakcji > najwieksza_ilosc_biletow_w_transakcji:
        najwieksza_ilosc_biletow_w_transakcji = liczba_biletow_w_transakcji
        transakcja_z_najwieksza_iloscia = transakcja + 1

# Ustalanie ceny biletu na podstawie sumy
if liczba_biletow_total >= 10:
    cena_biletu = 10
elif liczba_biletow_total >= 5:
    cena_biletu = 15
else:
    cena_biletu = 20

# Podsumowanie
print("\nPodsumowanie:")
print(f"Suma zakupionych biletów: {liczba_biletow_total}")
print(f"Kwota do zapłaty: {liczba_biletow_total * cena_biletu} zł")
print(f"Największa liczba zakupionych biletów w jednej transakcji: {najwieksza_ilosc_biletow_w_transakcji}")
print(f"Transakcja z największymi zakupami: osoba #{transakcja_z_najwieksza_iloscia}")
