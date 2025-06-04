from file_handler import file_handler, save_temporary_data

konto = file_handler.saldo
operacje_finansowe = file_handler.historia
magazyn = file_handler.magazyn

print("Witaj w programie księgowym! Zaczynamy?")
komenda = ["saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przegląd", "koniec"]
while True:
    print("Wybierz opcję:")
    print("1. saldo","\n2. sprzedaż","\n3. zakup","\n4. konto","\n5. lista","\n6. magazyn","\n7. przegląd","\n8. koniec")
    komenda = input("Wprowadź komendę (1-8): ")

    match komenda:
        case "1": #saldo
            try:
                kwota = float(input("Wprowadź kwotę (może być ujemna): "))
                konto += kwota
                operacje_finansowe.append(("saldo", kwota))
                if kwota < 0:
                    print("Masz debet na koncie!")
                save_temporary_data(file_handler, magazyn, konto, operacje_finansowe)

            except ValueError:
                print("Błąd! Wprowadzona wartość jest nie poprawna, spróbuj jeszcze raz.")

        case "2": #zakup
            try:
                produkt = input("Podaj nazwę produktu: ").strip().lower()
                producent = input("Podaj nazwę producenta: ").strip().lower()
                rodzaj = input("Podaj rodzaj produktu: ").strip().lower()
                ilosc = int(input("Podaj ilość: "))
                rok = int(input("Podaj rok produkcji: "))
                cena = float(input("Cena za sztukę: "))

                if cena <= 0 or ilosc <= 0 or rok < 1990:
                    print("Błąd: Cena, ilość lub rok są nieprawidłowe. Zakup anulowany.")
                    continue

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
                save_temporary_data(file_handler, magazyn, konto, operacje_finansowe)

            except ValueError:
                    print("Błąd: podano dane w nieprawidłowym formacie.")

        case "3": #sprzedaż
            try:
                produkt = input("Podaj nazwę produktu do sprzedaży: ").strip().lower()

                if produkt not in magazyn:
                    print("Podany produkt jest niedostępny w magazynie.")
                    continue

                ilosc = int(input("Podaj ilość sztuk do sprzedaży: "))

                if ilosc <= 0:
                    print("Ilość musi być większa niż 0.")
                    continue

                if magazyn[produkt]["ilosc"] < ilosc:
                    print(f"W magazynie jest tylko {magazyn[produkt]['ilosc']} sztuk.")
                    continue

                cena = magazyn[produkt]["cena"]
                przychod = cena * ilosc
                konto += przychod
                magazyn[produkt]["ilosc"] -= ilosc

                if magazyn[produkt]["ilosc"] == 0:
                    print(f"Produkt {produkt} jest teraz wyprzedany – brak sztuk na stanie.")

                operacje_finansowe.append(("sprzedaż", produkt, ilosc, cena))
                print(f"Sprzedano {ilosc} x {produkt} po {cena:.2f} zł = {przychod:.2f} zł")
                save_temporary_data(file_handler, magazyn, konto, operacje_finansowe)

            except ValueError:
                print("Błąd: podano nieprawidłową wartość.")

        case "4": #konto
            print(f"Aktualny budżet to: {konto:.2f} zł.")

        case "5": #lista
            if not magazyn:
                print("Magazyn jest pusty!")
            else:
                print("Stan magazynu:")
                for produkt, dane in magazyn.items():
                    print(f"{produkt.capitalize()} ({dane['producent'].capitalize()}) - {dane['ilosc']} szt. | cena: {dane['cena']:.2f} zł")

        case "6": #magazyn
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

        case "7": #przegląd
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

        case "8": #koniec
            print("Zakańczam działanie programu")
            break

file_handler.magazyn = magazyn
file_handler.saldo = konto
file_handler.historia = operacje_finansowe
file_handler.save_magazyn_file()
file_handler.save_saldo_file()
file_handler.save_historia_file()










