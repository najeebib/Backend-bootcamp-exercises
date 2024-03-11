def bumpy(distance, truck):
    truck_max_fuel = truck.get_max_fuel_amount()
    truck_km_per_liter = truck.get_km_per_liter()
    road_terrain_hardness = 1.2
    max_distance = (truck_max_fuel * truck_km_per_liter) / road_terrain_hardness
    if max_distance >= distance:
        return True
    else:
        return False
