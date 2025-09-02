# what is varable ??
# varible is contaner
# a=10

# b=45.5

# print(type(b))"


# name="juha"

# print(type(name))


# num="32"

# print(type(num))


# a=10
# b=45

# c=a+b

# print(c)



#string concatination  string haru ko add lai 
# a="b"

# b="c"

# d=a+b


# print(d)



# a=[1,2,3,4,5]


# print(type(a))



# b=(1,2,3,4,5)

# print(type(b))
# c={1,2,3,4,5}

# print(type(c))


# contact={"ajay":9800000000,"nirmal":9811111111,"ram":9822222222}


# print(type(contact))



#W lets make if else condition



# age=int(input("age han muji:"))



# if age>=18:
#     print("la muji ja vote garna ")



# else:
#     print("vaag muji ghar ja vote garna paunnas")





# a=True

# print(type(a))





# a=5.5


# b=int(a)   #explicitly deko type convo


# print(type(b))



#!/usr/bin/env python3
"""
House-Flipping Listings CLI
- Defines a Listing class (address: str, price: float + 3+ extra fields)
- CLI to:
  1) Print all listings
  2) Print a selected listing's info
  3) Purchase a house (removes it from active listings)
  4) (Optional) Create a new listing
"""

from dataclasses import dataclass, field
from typing import ClassVar, Dict, Optional


@dataclass
class Listing:
    """Represents a single house listing in a flipping service."""
    address: str
    price: float
    bedrooms: int
    bathrooms: float
    square_feet: int

    # Auto-managed fields
    id: int = field(init=False)
    is_active: bool = field(default=True)

    # Class-level ID generator
    _next_id: ClassVar[int] = 1

    def __post_init__(self) -> None:
        # Assign unique, auto-incrementing ID
        self.id = Listing._next_id
        Listing._next_id += 1

        # Basic validation to emphasize class-object correctness
        if not isinstance(self.address, str) or not self.address.strip():
            raise ValueError("address must be a non-empty string.")
        if not isinstance(self.price, (int, float)):
            raise TypeError("price must be a float.")
        if float(self.price) <= 0:
            raise ValueError("price must be positive.")
        if not isinstance(self.bedrooms, int) or self.bedrooms < 0:
            raise ValueError("bedrooms must be a non-negative integer.")
        if not isinstance(self.bathrooms, (int, float)) or self.bathrooms < 0:
            raise ValueError("bathrooms must be a non-negative number.")
        if not isinstance(self.square_feet, int) or self.square_feet <= 0:
            raise ValueError("square_feet must be a positive integer.")

        # Normalize types
        self.price = float(self.price)
        self.bathrooms = float(self.bathrooms)

    def purchase(self) -> None:
        """Marks the listing as sold; caller should remove from active store."""
        if not self.is_active:
            raise ValueError("This listing is already sold/unlisted.")
        self.is_active = False

    def short_line(self) -> str:
        status = "ACTIVE" if self.is_active else "SOLD"
        return f"[{self.id}] {self.address} — €{self.price:,.2f} — {self.bedrooms}bd/{self.bathrooms}ba — {self.square_feet} sqft — {status}"

    def detail(self) -> str:
        lines = [
            f"Listing ID:       {self.id}",
            f"Address:          {self.address}",
            f"Price:            €{self.price:,.2f}",
            f"Bedrooms:         {self.bedrooms}",
            f"Bathrooms:        {self.bathrooms}",
            f"Square Feet:      {self.square_feet}",
            f"Status:           {'ACTIVE' if self.is_active else 'SOLD'}",
        ]
        return "\n".join(lines)


class ListingSystem:
    """In-memory store and CLI operations for listings."""
    def __init__(self) -> None:
        self._active: Dict[int, Listing] = {}

    def add_listing(self, listing: Listing) -> None:
        if not listing.is_active:
            raise ValueError("Cannot add an inactive listing.")
        self._active[listing.id] = listing

    def all_listings(self) -> Dict[int, Listing]:
        # Only active ones are "in the system"
        return dict(self._active)

    def get_listing(self, listing_id: int) -> Optional[Listing]:
        return self._active.get(listing_id)

    def purchase(self, listing_id: int) -> Listing:
        listing = self.get_listing(listing_id)
        if listing is None:
            raise KeyError(f"No active listing found with ID {listing_id}.")
        listing.purchase()
        # Remove from the system (becomes unlisted)
        self._active.pop(listing_id, None)
        return listing


# ---------- CLI Helpers ----------

def prompt_menu() -> str:
    print("\n=== House-Flipping Listings ===")
    print("1) Print ALL listings")
    print("2) Print a SELECTED listing's info")
    print("3) PURCHASE a house (removes from system)")
    print("4) Create a NEW listing (optional)")
    print("5) Quit")
    return input("Choose an option [1-5]: ").strip()


def read_int(prompt: str, allow_zero: bool = False) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if not allow_zero and val <= 0:
                print("Please enter a positive integer.")
                continue
            return val
        except ValueError:
            print("Invalid integer. Try again.")


def read_float(prompt: str, positive: bool = True) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if positive and val <= 0:
                print("Please enter a positive number.")
                continue
            return val
        except ValueError:
            print("Invalid number. Try again.")


def read_str(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Please enter a non-empty value.")


def seed_data(system: ListingSystem) -> None:
    # Add a few sample active listings to work with
    samples = [
        Listing("123 Maple St, Espoo", 299000.0, bedrooms=3, bathrooms=1.5, square_feet=1100),
        Listing("45 Birch Ave, Helsinki", 449500.0, bedrooms=4, bathrooms=2.0, square_feet=1650),
        Listing("9 Oak Lane, Vantaa", 375000.0, bedrooms=3, bathrooms=2.0, square_feet=1400),
    ]
    for l in samples:
        system.add_listing(l)


def cmd_print_all(system: ListingSystem) -> None:
    listings = system.all_listings()
    if not listings:
        print("\n(No active listings in the system.)")
        return
    print("\nActive Listings:")
    for lst in listings.values():
        print(" - " + lst.short_line())


def cmd_print_one(system: ListingSystem) -> None:
    listing_id = read_int("Enter Listing ID to view: ")
    listing = system.get_listing(listing_id)
    if listing is None:
        print(f"\nNo active listing found with ID {listing_id}.")
        return
    print("\n" + listing.detail())


def cmd_purchase(system: ListingSystem) -> None:
    listing_id = read_int("Enter Listing ID to PURCHASE: ")
    try:
        purchased = system.purchase(listing_id)
        print("\nPurchase successful. Removed from active listings.")
        print(purchased.detail())
    except KeyError as e:
        print(f"\n{e}")
    except ValueError as e:
        # e.g., attempting to purchase an already-sold listing (shouldn't occur since we drop it)
        print(f"\nPurchase failed: {e}")


def cmd_create(system: ListingSystem) -> None:
    print("\nEnter new listing details:")
    address = read_str(" Address: ")
    price = read_float(" Price (EUR): ", positive=True)
    bedrooms = read_int(" Bedrooms (integer): ", allow_zero=True)
    bathrooms = read_float(" Bathrooms (e.g., 1.5): ", positive=True)
    square_feet = read_int(" Square feet (integer): ")

    try:
        listing = Listing(
            address=address,
            price=price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            square_feet=square_feet,
        )
        system.add_listing(listing)
        print("\nNew listing created:")
        print(listing.detail())
    except (TypeError, ValueError) as e:
        print(f"\nFailed to create listing: {e}")


def main() -> None:
    system = ListingSystem()
    seed_data(system)  # Pre-populate a few listings

    while True:
        choice = prompt_menu()
        if choice == "1":
            cmd_print_all(system)
        elif choice == "2":
            cmd_print_one(system)
        elif choice == "3":
            cmd_purchase(system)
        elif choice == "4":
            cmd_create(system)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()













