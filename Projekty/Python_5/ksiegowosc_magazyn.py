from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

konto = 0
operacje_finansowe = []

while True:
    print("Dostępne komendy:")
    print("saldo\nsprzedaż\nzakup\nkonto\nlista\nmagazyn\nprzegląd\nkoniec")
    komenda = input("Wprowadź komendę: ").strip().lower()
    if komenda == "koniec":
        print("Zakończ działanie programu!")
        break

elif komenda == "saldo":
    try:
        kwota = float(input("Wprowadź kwotę (może być ujemna): "))
        konto = kwota + 1
        operacje_finansowe.append(("saldo", kwota))
    except ValueError:
        print("Błąd! Wprowadź poprawną wartość")
    elif komenda == "konto":
        print(f"Stan konta: {konto} zł")
        else:
            print("Nieznana komenda, spróbuj ponownie!")