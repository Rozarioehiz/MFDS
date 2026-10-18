from fuelDispenser.Dispenser import Dispenser


def station():
    dispenser = Dispenser()
    dispenser.add_fuel("Petrol", 650, 1000)
    dispenser.add_fuel("Diesel", 720, 1000)
    dispenser.add_fuel("Kerosene", 550, 1000)
    dispenser.add_fuel("Gas", 480, 1000)
    return dispenser


def read_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a number.")


def show_fuels(attendant):
    print("\n--- Available Fuels ---")
    for fuel in attendant.get_available_fuel():
        print(f"{fuel.fuel_name:<10} ₦{fuel.price_per_liter} per liter")


def buy_fuel(attendant):
    show_fuels(attendant)
    fuel_name = input("Choose fuel: ")
    choice = input("Buy by (1) Liters or (2) Amount? ")
    try:
        if choice == "1":
            liters = read_number("Liters (1 - 50): ")
            transaction = attendant.dispense_fuel_by_liters(fuel_name, liters)
        elif choice == "2":
            amount = read_number("Amount (₦): ")
            transaction = attendant.dispense_fuel_by_amount(fuel_name, amount)
        else:
            print("Invalid choice.")
            return
        print(attendant.generate_receipt(transaction))
    except ValueError as error:
        print(f"Error: {error}")


def show_transactions(attendant):
    transactions = attendant.show_all_transactions()
    if not transactions:
        print("No transactions yet.")
    for t in transactions:
        print(f"{t['date']} | {t['fuel_name']} | {t['liters']}L | ₦{t['amount']:,.2f}")


def attendant_menu(attendant):
    print("\n1. Add new fuel  2. Update price  3. Restock")
    choice = input("Choose: ")
    try:
        if choice == "1":
            attendant.add_new_fuel(input("Name: "), read_number("Price: "), read_number("Liters: "))
        elif choice == "2":
            attendant.update_fuel_price(input("Fuel: "), read_number("New price: "))
        elif choice == "3":
            attendant.restock_fuel(input("Fuel: "), read_number("Liters to add: "))
        else:
            print("Invalid choice.")
            return
        print("Done.")
    except ValueError as error:
        print(f"Error: {error}")


def main():
    attendant = FuelAttendant("Rose", station())
    print("Welcome to GBeda Station")
    while True:
        print("\n1. Buy Petroleum  2. Show Transaction History  3. Attendant Menu  4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            buy_fuel(attendant)
        elif choice == "2":
            show_transactions(attendant)
        elif choice == "3":
            attendant_menu(attendant)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()