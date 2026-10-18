import unittest
from fuel.Fuel import Fuel


class FuelTest(unittest.TestCase):
    def test_fuel_is_created_with_details(self):
        fuel = Fuel("Petrol", 650, 100)
        self.assertEqual("Petrol", fuel.fuel_name)
        self.assertEqual(650, fuel.price_per_liter)
        self.assertEqual(100, fuel.quantity)

    def test_quantity_is_zero(self):
        fuel = Fuel("Petrol", 650)
        self.assertEqual(0, fuel.quantity)

    def test_no_amount_raises_error(self):
        with self.assertRaises(ValueError):
            Fuel("Petrol", 0, 100)

    def test_negative_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            Fuel("Petrol", 650, -1)

    def test_update_price(self):
        fuel = Fuel("Petrol", 650, 100)
        fuel.update_price(700)
        self.assertEqual(700, fuel.price_per_liter)

    def test_update_price_to_zero_raises_error(self):
        fuel = Fuel("Petrol", 650, 100)
        with self.assertRaises(ValueError):
            fuel.update_price(0)

    def test_restock_adds_to_quantity(self):
        fuel = Fuel("Petrol", 650, 100)
        fuel.restock(50)
        self.assertEqual(150, fuel.quantity)

    def test_restock_zero_raises_error(self):
        fuel = Fuel("Petrol", 650, 100)
        with self.assertRaises(ValueError):
            fuel.restock(0)

    def test_reduce_quantity(self):
        fuel = Fuel("Petrol", 650, 100)
        fuel.reduce_quantity(30)
        self.assertEqual(70, fuel.quantity)

    # def test_reduce_more_than_stock_raises_error(self):
    #     fuel = Fuel("Petrol", 650, 10)
    #     with self.assertRaises(ValueError):
    #         fuel.reduce_quantity(11)


if __name__ == "__main__":
    unittest.main()