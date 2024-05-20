from abc import ABC, abstractmethod
from datetime import datetime

# Absztrakt szoba osztály
class Szoba(ABC):
    def __init__(self, price, room_number):
        self.price = price
        self.room_number = room_number

    @abstractmethod
    def room_type(self):
        pass

# Egyágyas szoba osztály
class Egyagyas(Szoba):
    def __init__(self, price, room_number):
        super().__init__(price, room_number)

    def room_type(self):
        return "Egyágyas"

# Kétágyas szoba osztály
class Ketagyas(Szoba):
    def __init__(self, price, room_number):
        super().__init__(price, room_number)

    def room_type(self):
        return "Kétágyas"

# Hotel osztály
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

# Foglalás osztály
class Foglalas:
    def __init__(self):
        self.bookings = {}

    def book_room(self, room, date):
        if date in self.bookings and room in self.bookings[date]:
            return f"A {room.room_number} számú szoba már foglalt ebben az időpontban: {date}"
        if date not in self.bookings:
            self.bookings[date] = []
        self.bookings[date].append(room)
        return f"A {room.room_number} számú szoba le lett foglalva a következő időpontra: {date}"

    def cancel_booking(self, room, date):
        if date in self.bookings and room in self.bookings[date]:
            self.bookings[date].remove(room)
            return f"A foglalás {room.room_number} számú szobára, {date} időpontra törölve lett."
        return "A foglalás nem található."

    def list_bookings(self):
        return self.bookings

# Ebben a részben történik az egyágyas, illetve a kétágyas szobák létrehozása
def szoba_generalas(hotel):
    # Add single rooms
    for i in range(1, 11):  # 10 darab egyágyas szobát készít
        room = Egyagyas(100, 100 + i)
        hotel.add_room(room)

    # Add double rooms
    for i in range(1, 11):  # 10 darab kétágyas szobát készít
        room = Ketagyas(200, 200 + i)
        hotel.add_room(room)

    print(f"Összesen {len(hotel.rooms)} lett generálva.")

# Felhasználói felület
def user_interface():
    hotel = Hotel("Grand Budapest")
    booking_system = Foglalas()

    # Szobák létrehozása
    szoba_generalas(hotel)

    while True:
        print("1. Szoba foglalás")
        print("2. Foglalás törlése")
        print("3. Az összes szoba listázása")
        print("4. Foglalások listázása")
        print("5. Kilépés")
        choice = int(input("Válasszon egyet a fenti lehetőségek közül: "))

        if choice == 1:
            room_number = int(input("Írja a be a szoba sorszámát: "))
            date = input("Írja be a foglalás időpontját (YYYY-MM-DD): ")
            date = datetime.strptime(date, "%Y-%m-%d").date()

            room = next((r for r in hotel.rooms if r.room_number == room_number), None)
            if room:
                print(booking_system.book_room(room, date))
            else:
                print("A szoba nem található")

        elif choice == 2:
            room_number = int(input("Írja a be a szoba sorszámát: "))
            date = input("Írja be a foglalás időpontját (YYYY-MM-DD): ")
            date = datetime.strptime(date, "%Y-%m-%d").date()

            room = next((r for r in hotel.rooms if r.room_number == room_number), None)
            if room:
                print(booking_system.cancel_booking(room, date))
            else:
                print("A szoba nem található")

        elif choice == 3:
            for room in hotel.rooms:
                print(f"Szoba {room.room_number}: {room.room_type()} - Ár: {room.price}")

        elif choice == 4:
            bookings = booking_system.list_bookings()
            for date, rooms in bookings.items():
                print(f"Időpont: {date}")
                for room in rooms:
                    print(f"  Szoba {room.room_number} ({room.room_type()})")

        elif choice == 5:
            break

        else:
            print("Nincs ilyen lehetőség, kérem válasszon egy másikat.")

if __name__ == "__main__":
    user_interface()