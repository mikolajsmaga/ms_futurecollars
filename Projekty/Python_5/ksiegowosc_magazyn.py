
print("Witaj w programie księgowym! Zaczynamy?")

konto = 1000.0 #Stan konta
operacje_finansowe = []
komenda = ["saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przegląd", "koniec"]
magazyn = {
    "laptop": {
        "producent": "Dell",
        "rok": 2023,
        "rodzaj": "Elektronika",
        "ilosc": 5,
        "cena": 3000.0
    },
    "monitor": {
        "producent": "LG",
        "rok": 2022,
        "rodzaj": "Elektronika",
        "ilosc": 2,
        "cena": 800.0
    },
    "klawiatura": {
        "producent": "Logitech",
        "rok": 2025,
        "rodzaj": "Elektronika",
        "ilosc": 10,
        "cena": 750.0
    }
}
while True:
    print("Dostępne komendy:")
    print("1. saldo","\n2. sprzedaż","\n3. zakup","\n4. konto","\n5. lista","\n6. magazyn","\n7. przegląd","\n8. koniec")
    komenda = int(input("Wprowadź komendę: ")) #.strip().lower()
    if komenda == "koniec":
        print("Zakończ działanie programu!")
        break

    match komenda:
        case "saldo": #saldo
            try:
                kwota = float(input("Wprowadź kwotę (może być ujemna): "))
                konto += kwota
                operacje_finansowe.append(("saldo", kwota))
                if kwota < 0:
                    print("Masz debet na koncie!")

            except ValueError:
                print("Błąd! Wprowadzona wartość jest nie poprawna, spróbuj jeszcze raz.")
        case "zakup":
            try:
                produkt = input("Podaj nazwę produktu: ").strip().lower()
                producent = input("Podaj nazwę producenta: ").lower().lower()
                rodzaj = input("Podaj rodzaj produktu: ").lower().lower()
                ilosc = int(input("Podaj ilość: "))
                rok = int(input("Podaj rok: "))
                cena = float(input("Cena za sztukę: "))

                if cena <= 0 or ilosc <= 0 or rok < 1990:
                    print("Błąd: Cena, ilość lub rok są nieprawidłowe. Zakup anulowany.")
                    break

                koszt = cena * ilosc
                if konto < koszt:
                    print("Nie masz wystarczających środków na zakup!")
                    break

                konto -= koszt
                if produkt in magazyn:
                    magazyn[produkt]["ilosc"] += ilosc
                    magazyn[produkt]["cena"] = cena
                else:
                    magazyn[produkt] = {
                        "producent": producent,
                        "rok": rok,
                        "rodzaj": rodzaj,
                        "ilosc": ilosc,
                        "cena": cena,
                    }

                operacje_finansowe.append(("zakup", produkt, producent, rok, rodzaj, cena, ilosc))
                print(f"Zakupiono {ilosc} * {produkt} za {koszt:.2f} zł")

            except ValueError:
                    print("Błąd: podano dane w nieprawidłowym formacie.")

        case "sprzedaż":
            try:
                produkt = input("Podaj nazwę produktu do sprzedaży: ").strip().lower()

                if produkt not in magazyn:
                    print("❌ Podany produkt jest niedostępny w magazynie.")
                    continue

                ilosc = int(input("Podaj ilość sztuk do sprzedaży: "))

                if ilosc <= 0:
                    print("❌ Ilość musi być większa niż 0.")
                    continue

                if magazyn[produkt]["ilosc"] < ilosc:
                    print(f"❌ W magazynie jest tylko {magazyn[produkt]['ilosc']} sztuk.")
                    continue

                cena = magazyn[produkt]["cena"]
                przychod = cena * ilosc
                konto += przychod
                magazyn[produkt]["ilosc"] -= ilosc

                if magazyn[produkt]["ilosc"] == 0:
                    print(f"ℹ️ Produkt {produkt} jest teraz wyprzedany – brak sztuk na stanie.")

                operacje_finansowe.append(("sprzedaż", produkt, ilosc, cena))
                print(f"✅ Sprzedano {ilosc} x {produkt} po {cena:.2f} zł = {przychod:.2f} zł")

            except ValueError:
                print("❌ Błąd: podano nieprawidłową wartość.")

        case "konto":
            print(f"Aktualny budżet to: {konto:.2f} zł.")

        case "lista":
            if not magazyn:
                print("Magazyn jest pusty!")
            else:
                print("Stan magazynu:")
                for produkt, dane in magazyn.items():
                    print(f"{produkt} {dane['producent']} stan: {dane['ilosc']} sztuki na magazynie, cena {dane['cena']:.2f} zł")

        case "magazyn":
            produkt = input("Podaj nazwę produktu do wyświetlenia: ").strip().lower()
            if produkt in magazyn:
                dane = magazyn[produkt]
                print(f"Produkt: {produkt.capitalize()}")
                print(f"Producent: {dane['producent'].capitalize()}")
                print(f"Rok produkcji: {dane['rok']}")
                print(f"Rodzaj produktu: {dane['rodzaj'].capitalize()}")
                print(f"Ilość na magazynie: {dane['ilosc']}")
                print(f"Cena za sztukę: {dane['cena']:.2f} zł")
            else:
                print(f"Produkt '{produkt}' nie jest dostępny na magazynie.")

        case "przegląd":
            od = input("Podaj wartość 'od' (numer transakcji): ")
            do = input("Podaj wartość 'do' (numer transakcji): ")
            if od:
                od = int(od)
            else:
                od = 0
            if do:
                do = int(do)
            else:
                do = len(operacje_finansowe)
            print(operacje_finansowe[od:do])

        case "koniec":
            print("Zakańczam działanie programu")
            break










#print(f"Twój stan konta: {konto}")
