class Fuel:

    def __init__(self, fuel_name, price_per_liter, quantity = 0):

        self.fuel_name = fuel_name
        self.price_per_liter = price_per_liter
        self.quantity = quantity

        if price_per_liter <= 0:
            raise ValueError("Price per liter must be greater than 0")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

    def calculate_cost(self, liters):
        return liters * self.price_per_liter

    def calculate_liters(self, amount):
        return round(amount / self.price_per_liter, 2)

    def has_enough(self, liters):
        return self.quantity >= liters

    def reduce_quantity(self, liters):
        if not self.has_enough(liters):
            raise ValueError(f"Not enough {self.fuel_name} in stock")
        self.quantity -= liters

    def add_quantity(self, liters):
        if liters <= 0:
            raise ValueError("Restock liters must be greater than 0")
        self.quantity += liters

    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("Price per liter must be greater than 0")
        self.price_per_liter = new_price





