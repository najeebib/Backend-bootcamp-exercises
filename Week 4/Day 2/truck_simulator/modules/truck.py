class Truck:
    def __init__(self, max_fuel_amount, km_per_liter, price_repair_per_km, brand):
        self._max_fuel_amount = max_fuel_amount
        self._km_per_liter = km_per_liter
        self._price_repair_per_km = price_repair_per_km
        self._brand = brand

    def get_max_fuel_amount(self):
        return self._max_fuel_amount
    
    def get_km_per_liter(self):
        return self._km_per_liter

    def get_price_repair_per_km(self):
        return self._price_repair_per_km

    def get_brand(self):
        return self._brand