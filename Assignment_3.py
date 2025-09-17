"""
Assignment 3 — Listing CLI which i made for continue of assignment 
Author: Ghanshyam Bhattarai
Note: simple CLI for houses, furniture and perishables.
I wrote this to practice OOP (inheritance + encapsulation).
"""


# I had imported datetime so that i can check the expiry of perishable items 

from datetime import datetime
from typing import List, Optional


# small helper classes to keep item,specific data together
# i have made this class name Nap which is in meaning measure in english 
class Nap:
    def __init__(self, widh_cm: float, deapth_cm: float, height_cm: float):

        # i have made this  private attributes so that it can not be accessed directly
        self.__w = float(widh_cm)
        self.__d = float(deapth_cm)
        self.__h = float(height_cm)

    def __str__(self):
        return f"{self.__w}x{self.__d}x{self.__h} cm"

# helper class for perishable items , to check it is expred or not 
class ExpiryInfo:
    def __init__(self, best_before: str, storage_c: float):
        # i shold be in this format  "YYYY-MM-DD" format
        self.__best_before = best_before.strip()
        self.__storage_c = float(storage_c)

    def is_expired(self) -> bool:
        try:
            date_obj = datetime.strptime(self.__best_before, "%Y-%m-%d").date()
            return date_obj < datetime.today().date()
        except ValueError:
            # if date is invalid provieded , maKae as not knwing  (not expired)
            return False

    def __str__(self):
        state = "expired" if self.is_expired() else "valid"
        return f"best before {self.__best_before} | keep at {self.__storage_c}°C | {state}"


# Base class or parent class,shared paramters stays  here
class Listing:
    __id_counter = 1  # private class counter for unique ids

    def __init__(self, title: str, price: float):
        self.__id = Listing.__id_counter
        Listing.__id_counter += 1

        self.__title = title.strip()
        self.__price = float(price)

    # getter methods for private fields
    def get_id(self) -> int:
        return self.__id

    def get_title(self) -> str:
        return self.__title

    # use property for price so subclasses and code can set it safely
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price):
        try:
            v = float(new_price)
            if v >= 0:
                self.__price = v
            else:
                print("price not changed (negative)")
        except (TypeError, ValueError):
            print("price not changed (not a number)")

    def _kind(self) -> str:
        return "Listing"

    def __str__(self) -> str:
        return f"[{self.__id}] {self._kind()} | {self.__title} | Price: €{self.__price:,.2f}"


# subclasses with category,specific data
class HouseListing(Listing):
    def __init__(self, title: str, price: float, address: str, bedrooms: int, bathrooms: int, size_sqft: int):
        super().__init__(title, price)
        self.__address = address.strip()
        self.__bedrooms = int(bedrooms)
        self.__bathrooms = int(bathrooms)
        self.__size_sqft = int(size_sqft)

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, new_address: str):
        if isinstance(new_address, str) and new_address.strip():
            self.__address = new_address.strip()
        else:
            print("address not changed (empty)")

    def _kind(self) -> str:
        return "House"

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | {self.__address} | {self.__bedrooms} bd / {self.__bathrooms} ba | {self.__size_sqft} sqft"


class FurnitureListing(Listing):
    def __init__(self, title: str, price: float, material: str, condition_note: str, dims: Nap):
        super().__init__(title, price)
        self.__material = material.strip()
        self.__condition_note = condition_note.strip()
        self.__dims = dims  # composition

    def _kind(self) -> str:
        return "Furniture"

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | material: {self.__material} | condition: {self.__condition_note} | size: {self.__dims}"


class PerishableListing(Listing):
    def __init__(self, title: str, price: float, quantity: str, expiry: ExpiryInfo):
        super().__init__(title, price)
        self.__quantity = quantity.strip()
        self.__expiry = expiry

    def _kind(self) -> str:
        return "Perishable"

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | qty: {self.__quantity} | {self.__expiry}"


# bucket for storage  of all listings
listings: List[Listing] = []


# Helper to find listing by id
def _find_by_id(lid: int) -> Optional[Listing]:
    for l in listings:
        if l.get_id() == lid:
            return l
    return None


# i have made some changes in the below functions like show_all,show_one,buy_item,add_listing,edit_listing and menu function
def show_all():
    if not listings:
        print("No listings available.")
        return
    for l in listings:
        print(l)


def show_one():
    try:
        lid = int(input("Enter listing Id: "))
    except ValueError:
        print("wrong input.")
        return
    l = _find_by_id(lid)
    if l:
        print(l)
    else:
        print("Listing not found.")


def buy_item():
    try:
        lid = int(input("Enter listing Id to buy: "))
    except ValueError:
        print("wrong input.")
        return
    l = _find_by_id(lid)
    if l:
        listings.remove(l)
        print("Item purchased and removed from listings.")
    else:
        print("Listing not found.")


def add_listing():
    print("\nAdd which type?")
    print("1) House")
    print("2) Furniture")
    print("3) Perishable")
    t = input("Choose: ").strip()

    if t == "1":
        title = input("Title (e.g. 'Jholey 2MR'): ")
        try:
            price = float(input("Price (€): "))
            address = input("Address: ")
            bedrooms = int(input("Bedrooms: "))
            bathrooms = int(input("Bathrooms: "))
            size = int(input("Size (sqft): "))
        except ValueError:
            print("Please enter numbers for price/bedrooms/bathrooms/size.")
            return
        new_listing = HouseListing(title, price, address, bedrooms, bathrooms, size)

    elif t == "2":
        title = input("Title (e.g. 'Sisau desk'): ")
        try:
            price = float(input("Price (€): "))
            material = input("Material: ")
            cond = input("Condition note: ")
            w = float(input("Width (cm): "))
            d = float(input("Depth (cm): "))
            h = float(input("Height (cm): "))
        except ValueError:
            print("Please enter numbers for price/size.")
            return
        new_listing = FurnitureListing(title, price, material, cond, Nap(w, d, h))

    elif t == "3":
        title = input("Title (e.g. 'Sheu'): ")
        try:
            price = float(input("Price (€): "))
            qty = input("Quantity (e.g. '2 kg'): ")
            bb = input("Best before (YYYY-MM-DD): ")
            st = float(input("store temp (°C): "))
        except ValueError:
            print("Please enter numbers for price/storage.")
            return
        new_listing = PerishableListing(title, price, qty, ExpiryInfo(bb, st))

    else:
        print("Mistake choice bro .")
        return

    listings.append(new_listing)
    print("Listing added:", new_listing)


def edit_listing():
    print("\nEdit options:")
    print("1) Edit price (any listing)")
    print("2) Edit address (only House)")
    print("0) Cancel")
    c = input("Choose: ").strip()

    if c == "1":
        try:
            lid = int(input("Enter listing Id: "))
        except ValueError:
            print("Invalid input.")
            return
        l = _find_by_id(lid)
        if not l:
            print("Listing not found.")
            return
        new_p = input("New price: ")
        l.price = new_p  # used @property.setter in base class
        print("Updated:", l)

    elif c == "2":
        try:
            lid = int(input("Enter house Id: "))
        except ValueError:
            print("Invalid input.")
            return
        l = _find_by_id(lid)
        if not isinstance(l, HouseListing):
            print("That id is not a House listing (or not found).")
            return
        new_a = input("New address: ")
        l.address = new_a  # uses @property.setter in subclass
        print("Updated:", l)

    elif c == "0":
        print("Cancelled.")
    else:
        print("Mistake choice.")


def menu():
    while True:
        print("\n- Mero  Marketplace -")
        print("1) Show all listings")
        print("2) Show one listing")
        print("3) Buy an item (remove)")
        print("4) Add a listing")
        print("5) Edit a listing")
        print("0) Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            show_all()
        elif choice == "2":
            show_one()
        elif choice == "3":
            buy_item()
        elif choice == "4":
            add_listing()
        elif choice == "5":
            edit_listing()
        elif choice == "0":
            print("Bye-Bye, Mero Marketplace.")
            break
        else:
            print("Go TO hell, incorrect choice bro.")


if __name__ == "__main__":
    # starter data for testing
    listings.append(HouseListing("Jholey 3BR", 199000, "123 Kathmandu", 3, 2, 1500))
    listings.append(FurnitureListing("Sisau desk", 120, "Pine", "minor scratches", Nap(120, 60, 75)))
    listings.append(PerishableListing("Sheu", 1.29, "1 L", ExpiryInfo("2025-10-05", 4.0)))

menu()
