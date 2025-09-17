


# i am going to make a simple housing application in cli 

class Listing:
    
    _id_counter = 1  # will auto increase IDs

    def __init__(self, address: str, price: float, bedrooms: int, bathrooms: int, size: int):
        # private attributes 

        # The idea is some data inside an objecet should not be changesad from outside
        self.__id = Listing._id_counter
        Listing._id_counter += 1

        self.__address = address
        self.__price = price
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__size = size

    # getters
    def get_id(self):
        return self.__id

    def get_address(self):
        return self.__address

    def get_price(self):
        return self.__price

    def get_bedrooms(self):
        return self.__bedrooms

    def get_bathrooms(self):
        return self.__bathrooms

    def get_size(self):
        return self.__size

    def __str__(self):
        return f"[{self.__id}] {self.__address} | Price: {self.__price} | {self.__bedrooms} bd / {self.__bathrooms} ba | {self.__size} sqft"


# I made empty list for holdings values 
listings = []


# functions for CLI
def show_all():
    if not listings:
        print("No listings available.")
    else:
        for l in listings:
            print(l)


def show_one():
    try:
        lid = int(input("Enter listing Id: "))
        for l in listings:
            if l.get_id() == lid:
                print(l)
                return
        print("Listing not found.")
    except ValueError:
        print("Invalid input.")


def buy_house():
    try:
        lid = int(input("Enter listing Id to Purchase: "))
        for l in listings:
            if l.get_id() == lid:
                listings.remove(l)
                print("House Buyed and removed from listings.")
                return
        print("Listing not found.")
    except ValueError:
        print("Invalid input.")


def add_listing():
    address = input("Address: ")
    price = float(input("Price: "))
    bedrooms = int(input("Bedrooms: "))
    bathrooms = int(input("Bathrooms: "))
    size = int(input("Size (sqft): "))

    new_listing = Listing(address, price, bedrooms, bathrooms, size)
    listings.append(new_listing)
    print("Listing added:", new_listing)


def menu():
    while True:
        print("\n--- House Flipping Service ---")
        print("1) Show all listings")
        print("2) Show one listing")
        print("3) Buy a house")
        print("4) Add a listing")
        print("0) Exit")

        choice = input("Choose option: ")

        if choice == "1":
            show_all()
        elif choice == "2":
            show_one()
        elif choice == "3":
            buy_house()
        elif choice == "4":
            add_listing()
        elif choice == "0":
            print("sorry")
            break
        else:
            print("Incorrect choice.")


if __name__ == "__main__":
    # I have added some strter data to test which is my home country names 
    listings.append(Listing("123 Kathmandu ", 200000, 3, 2, 1500))
    listings.append(Listing("45 Pokharara", 350000, 4, 3, 2200))

    menu()
