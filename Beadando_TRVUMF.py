from abc import ABC, abstractmethod
from datetime import datetime

# Absztrakt szoba osztály
class Szoba(ABC):
    def __init__(self, ar, szoba_szam):
        self.ar = ar
        self.szoba_szam = szoba_szam

    @abstractmethod
    def szoba_type(self):
        pass

# Egyágyas szoba osztály
class Egyagyas(Szoba):
    def __init__(self, ar, szoba_szam):
        super().__init__(ar, szoba_szam)

    def szoba_type(self):
        return "Egyágyas"

# Kétágyas szoba osztály
class Ketagyas(Szoba):
    def __init__(self, ar, szoba_szam):
        super().__init__(ar, szoba_szam)

    def szoba_type(self):
        return "Kétágyas"

# Hotel osztály
class Hotel:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

# Foglalás osztály
class Foglalas:
    def __init__(self):
        self.foglalasok = {}

    def szoba_foglalas(self, szoba, datum):
        if datum in self.foglalasok and szoba in self.foglalasok[datum]:
            return f"A {szoba.szoba_szam} számú szoba már foglalt ebben az időpontban: {datum}"
        if datum not in self.foglalasok:
            self.foglalasok[datum] = []
        self.foglalasok[datum].append(szoba)
        return f"A {szoba.szoba_szam} számú szoba le lett foglalva a következő időpontra: {datum}"

    def szoba_torles(self, szoba, datum):
        if datum in self.foglalasok and szoba in self.foglalasok[datum]:
            self.foglalasok[datum].remove(szoba)
            return f"A foglalás {szoba.szoba_szam} számú szobára, {datum} időpontra törölve lett."
        return "A foglalás nem található."

    def lista_foglalasok(self):
        return self.foglalasok

# Ebben a részben történik az egyágyas, illetve a kétágyas szobák létrehozása
def szoba_generalas(hotel):
    # Egyágyas szobák hozzáadása
    for i in range(1, 11):  # 10 darab egyágyas szobát készít
        szoba = Egyagyas(100, 100 + i)
        hotel.add_szoba(szoba)

    # Kétágyas szobák hozzáadása
    for i in range(1, 11):  # 10 darab kétágyas szobát készít
        szoba = Ketagyas(200, 200 + i)
        hotel.add_szoba(szoba)

    print(f"Összesen {len(hotel.szobak)} lett generálva.")

# Felhasználói felület
def user_interface():
    hotel = Hotel("Grand Budapest")
    foglalas_rendszer = Foglalas()

    # Szobák létrehozása
    szoba_generalas(hotel)

    while True:
        print("1. Szoba foglalás")
        print("2. Foglalás törlése")
        print("3. Az összes szoba listázása")
        print("4. Foglalások listázása")
        print("5. Kilépés")
        m = int(input("Válasszon egyet a fenti lehetőségek közül: "))

        if m == 1:
            szoba_szam = int(input("Írja a be a szoba sorszámát: "))
            datum = input("Írja be a foglalás időpontját (YYYY-MM-DD): ")
            datum = datetime.strptime(datum, "%Y-%m-%d").date()

            szoba = next((r for r in hotel.szobak if r.szoba_szam == szoba_szam), None)
            if szoba:
                print(foglalas_rendszer.szoba_foglalas(szoba, datum))
            else:
                print("A szoba nem található")

        elif m == 2:
            szoba_szam = int(input("Írja a be a szoba sorszámát: "))
            datum = input("Írja be a foglalás időpontját (YYYY-MM-DD): ")
            datum = datetime.strptime(datum, "%Y-%m-%d").date()

            szoba = next((r for r in hotel.szobak if r.szoba_szam == szoba_szam), None)
            if szoba:
                print(foglalas_rendszer.szoba_torles(szoba, datum))
            else:
                print("A szoba nem található")

        elif m == 3:
            for szoba in hotel.szobak:
                print(f"Szoba {szoba.szoba_szam}: {szoba.szoba_type()} - Ár: {szoba.ar}")

        elif m == 4:
            foglalasok = foglalas_rendszer.lista_foglalasok()
            for datum, szobak in foglalasok.items():
                print(f"Időpont: {datum}")
                for szoba in szobak:
                    print(f"  Szoba {szoba.szoba_szam} ({szoba.szoba_type()})")

        elif m == 5:
            break

        else:
            print("Nincs ilyen lehetőség, kérem válasszon egy másikat.")

if __name__ == "__main__":
    user_interface()