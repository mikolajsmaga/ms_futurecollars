"""
Wczytaj od użytkownika:
- wiek (liczba całkowita),
- hasło dostępu (tekst),
- czy jest pracownikiem firmy (tak/nie).

Stwórz zmienne:
- has_prawidlowy_wiek (wiek >= 18),
- haslo_poprawne (hasło == "admin123"),
- jest_pracownikiem (tak/nie).

Dostęp przyznaj jeśli: (pełnoletni i poprawne hasło) lub (jest pracownikiem).

Wyświetl:
- "Dostęp przyznany" lub "Dostęp zabroniony", bez użycia ifów.
"""
#Logowanie
print("Logowanie")
wiek = int(input("Podaj wiek: "))
haslo = input("Podaj hasło: ")
pracownik_firmy = input("Czy jesteś pracownikiem firmy? (Tak/Nie): ")
pracownik_firmy = pracownik_firmy.lower()
#Sprawdzanie
twoj_prawidlowy_wiek = wiek >= 18
haslo_poprawne = haslo == "admin123"
jest_pracownikiem = pracownik_firmy == "tak"
#Argument Logiczny
dostep_przyznany = (twoj_prawidlowy_wiek and haslo_poprawne) or jest_pracownikiem
#Wynik
print(["Dostęp Zabroniony","Dostęp Przyznany"][dostep_przyznany])




