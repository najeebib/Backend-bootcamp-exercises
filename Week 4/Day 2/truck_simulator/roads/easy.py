import logging

def easy(distance, truck):
    truck_max_fuel = truck.get_max_fuel_amount()
    truck_km_per_liter = truck.get_km_per_liter()
    road_terrain_hardness = 1
    wheel_damage_effect = 0.01
    damage_to_wheels = distance * wheel_damage_effect
    print(f"Travelling on a easy road, the wheels will be damaged by {damage_to_wheels}%, the drivers mood will improve a bit")
    logging.info(f"Travelling on a easy road, the wheels will be damaged by {damage_to_wheels}%, the drivers mood will improve a bit")
    max_distance = (truck_max_fuel * truck_km_per_liter) / road_terrain_hardness
    if max_distance >= distance:
        return True
    else:
        return False
