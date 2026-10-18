from datetime import datetime

MIN_LITERS = 1
MAX_LITERS = 50


class FuelAttendant:

    def __init__(self, full_name, dispenser):
        self.full_name = full_name
        self.dispenser = dispenser
        self.transactions = []

    def add_new_fuel(self, fuel_name, price_per_liter, quantity):
        self.dispenser.add_fuel(fuel_name, price_per_liter, quantity)

    def get_available_fuel(self):
        return self.dispenser.get_available_fuels()

    def update_fuel_price(self, fuel_name, new_price):
        self.dispenser.get_fuel(fuel_name).update_price(new_price)

    def restock_fuel(self, fuel_name, liters):
        self.dispenser.get_fuel(fuel_name).add_quantity(liters)

    def dispense_fuel_by_liters(self, fuel_name, liters):
        if liters < MIN_LITERS or liters > MAX_LITERS:
            raise ValueError(f"Liters must be between {MIN_LITERS} and {MAX_LITERS}")
        fuel = self.dispenser.get_fuel(fuel_name)
        amount = fuel.calculate_cost(liters)
        return self._complete_sale(fuel, liters, amount)

    def dispense_fuel_by_amount(self, fuel_name, amount):
        fuel = self.dispenser.get_fuel(fuel_name)
        if amount <= fuel.price_per_liter:
            raise ValueError("Amount must be above the price of one liter")
        liters = fuel.calculate_liters(amount)
        if liters > MAX_LITERS:
            raise ValueError(f"That amount is more than {MAX_LITERS} liters")
        return self._complete_sale(fuel, liters, amount)

    def _complete_sale(self, fuel, liters, amount):
        fuel.reduce_quantity(liters)
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "attendant": self.full_name,
            "fuel_name": fuel.fuel_name,
            "price_per_liter": fuel.price_per_liter,
            "liters": liters,
            "amount": amount,
        }
        self.transactions.append(transaction)
        return transaction

    def show_all_transactions(self):
        return self.transactions

    def generate_receipt(self, transaction):
        return (
            "========== RECEIPT ==========\n"
            f"Date      : {transaction['date']}\n"
            f"Attendant : {transaction['attendant']}\n"
            f"Fuel      : {transaction['fuel_name']}\n"
            f"Price/L   : ₦{transaction['price_per_liter']}\n"
            f"Liters    : {transaction['liters']}\n"
            f"Amount    : ₦{transaction['amount']:,.2f}\n"
            "============================="
        )