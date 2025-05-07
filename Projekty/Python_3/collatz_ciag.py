"""
Ciąg Collatza zdefiniowany jest następująco:
Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100). #Integer i sprawdzanie
Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2. #warunek if
W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1. #else
W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1. #stwierdzenie ciag_liczb

Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
X może przyjmować wartości od 1 do 100.
"""

#Sprawdzanie poprawnosci
x = int(input("Podaj wartość całkowitą dla x (od 1 do 100): "))
if x < 1 or x > 100:
    print("Liczba musi być z zakresu od 1 do 100.")
else:
    dlugosc_ciagu = 1 #liczymy pierwszą wartosć

    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        dlugosc_ciagu = dlugosc_ciagu + 1 #dlugosc_ciagu += 1

    print(f"Długość ciągu Collatza: {dlugosc_ciagu}")
