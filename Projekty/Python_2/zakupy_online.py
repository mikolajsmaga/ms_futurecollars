"""
Zakupy online - rabaty

Wczytaj od użytkownika:
- czy zamówienie przekracza 100 zł (tak/nie),
- czy jest klientem VIP (tak/nie),
- czy kupił produkt promocyjny (tak/nie).

Rabat:
- 15% jeśli zamówienie >100 zł lub VIP,
- dodatkowe 5% jeśli produkt promocyjny.

Wyświetl "Twój rabat wynosi X%" bez użycia ifów.
"""


zamowienie = float(input("Podaj kwotę zamówienia: "))
zamowienie_powyzej_100 = zamowienie >= 100 or "tak"

vip = input("Czy jesteś klientem VIP? (tak/nie): ")
vip = vip.lower()
klient_vip = vip == "tak"

promocja = input("Czy kupiłeś produkt promocyjny? (tak/nie): ")
promocja = promocja.lower()
produkt_promocyjny = promocja == "tak"

rabat = 0.15 * (zamowienie_powyzej_100 or klient_vip) + 0.05 * produkt_promocyjny

print(f"Kwota przed rabatem: {zamowienie}")
print(f"Twoja kwota po rabatach: {zamowienie * (1 - rabat)}")
print(f"Przyznany rabat: {100 * rabat}%")



