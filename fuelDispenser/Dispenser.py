from fuel.Fuel import Fuel

#
# fuel ={
#     "Petroleum": ["petro","kerosene","gas","diseal"]
# }


from fuel.Fuel import Fuel


class Dispenser:

    def __init__(self):
        self.fuels = {}

    def add_fuel(self, fuel_name, price_per_liter, quantity):
        key = fuel_name.lower()
        if key == "":
            raise ValueError("Fuel name cannot be empty")
        if key in self.fuels:
            raise ValueError(f"{fuel_name} already exists")
        self.fuels[key] = Fuel(fuel_name.title(), price_per_liter, quantity)

    def get_fuel(self, fuel_name):
        key = fuel_name.lower()
        if key not in self.fuels:
            raise ValueError(f"{fuel_name} is not available")
        return self.fuels[key]

    def get_available_fuels(self):
        return [fuel for fuel in self.fuels.values() if fuel.quantity > 0]