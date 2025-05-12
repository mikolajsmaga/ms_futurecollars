
print("Witaj w programie księgowym! Zaczynamy?")

konto = 0.0
operacje_finansowe = []
komenda = ["saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przegląd", "koniec"]

while True:
    print("Dostępne komendy:")
    print("1. saldo","\n2. sprzedaż","\n3. zakup","\n4. konto","\n5. lista","\n6. magazyn","\n7. przegląd","\n8. koniec")
    komenda = input("Wprowadź komendę: ").strip().lower()
    if komenda == "koniec":
        print("Zakończ działanie programu!")
        break

    match komenda:
        case "saldo":
            kwota = float(input("Wprowadź kwotę (może być ujemna): "))
            konto += kwota
            operacje_finansowe.append(("saldo", kwota))
            if kwota < 0:
                print("Masz debet na koncie!")




print(f"Twój stan konta: {konto}")


























