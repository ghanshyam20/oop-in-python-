# very simple housing app in cli  (my second assignment)
# i try to follow viope: private members , properties + simple menu

class Listing:
    __id_counter = 1  # i made this  private class counter for id count sutoincrease

    def __init__(self, address: str, price: float, bedrooms: int, bathrooms: int, size: int):
        # private attributes
        self.__id = Listing.__id_counter
        Listing.__id_counter += 1

        self.__address = address
        self.__price = price
        self.__bedrooms = bedrooms
        self.__bathrooms = bathrooms
        self.__size = size

    # properties
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        # very basic check
        if isinstance(new_address, str) and new_address.strip() != "":
            self.__address = new_address.strip()
        else:
            print("address not changed (empty)")

    @property
    def price(self):
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

    # classic getters 
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


# I made empty list for storinng all values 
listings = []


#CLI functions 
def show_all():
    if not listings:
        print("No listings avialable.")
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
        print("Listing not find.")
    except ValueError:
        print("worng input.")


def buy_house():
    try:
        lid = int(input("Enter listing Id to buy: "))
        for l in listings:
            if l.get_id() == lid:
                listings.remove(l)
                print("House Buyed and removed from listings.")
                return
        print("Listing not founds.")
    except ValueError:
        print("wrong input.")


def add_listing():
    address = input("Address: ")
    try:
        price = float(input("Price: "))
        bedrooms = int(input("Bedrooms: "))
        bathrooms = int(input("Bathrooms: "))
        size = int(input("Size (sqft): "))
    except ValueError:
        print("Please enter numbers for price/bedrooms/bathrooms/size.")
        return

    new_listing = Listing(address, price, bedrooms, bathrooms, size)
    listings.append(new_listing)
    print("Listing added:", new_listing)


def edit_listing():
  
    try:
        lid = int(input("Enter listing Id to Edit: "))
    except ValueError:
        print("Invalid input.")
        return

    target = None
    for l in listings:
        if l.get_id() == lid:
            target = l
            break

    if target is None:
        print("Listing not found.")
        return

    print("Edit options: 1) Address  2) Price  0) Cancels")
    choice = input("Choose: ").strip()

    if choice == "1":
        new_addr = input("New address: ")
        target.address = new_addr   #  i uses @address.setter
        print("Updated:", target)
    elif choice == "2":
        new_price = input("New price: ")
        target.price = new_price    # i uses @price.setter
        print("Updated:", target)
    elif choice == "0":
        print("Cancelled.")
    else:
        print("Mistake choice.")


def menu():
    while True:
        print("\n- House Flipping Service -")
        print("1) Show all listings")
        print("2 Show one listing")
        print("3) Buy a house")
        print("4) Add a listing")
        print("5 Edit a listing (address/price)")  # i proivderd  new option for properties
        print("0) Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            show_all()
        elif choice == "2":
            show_one()
        elif choice == "3":
            buy_house()
        elif choice == "4":
            add_listing()
        elif choice == "5":
            edit_listing()
        elif choice == "0":
            print("go hell fiend ")
            break
        else:
            print("Incorrect choice.")


if __name__ == "__main__":
    # I have added some strter data to check which is my home country names
    listings.append(Listing("123 Kathmandu", 200000, 3, 2, 1500))
    listings.append(Listing("45 Pokhara", 350000, 4, 3, 2200))
    menu()
