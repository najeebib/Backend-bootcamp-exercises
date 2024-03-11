import logging

def hard(distance, truck):
    truck_max_fuel = truck.get_max_fuel_amount()
    truck_km_per_liter = truck.get_km_per_liter()
    road_terrain_hardness = 1.5
    max_distance = (truck_max_fuel * truck_km_per_liter) / road_terrain_hardness
    wheel_damage_effect = 0.01
    damage_to_wheels = distance * wheel_damage_effect
    print(f"Travelling on a hard road, the wheels will be damaged by {damage_to_wheels}%, the drivers mood will decrease slightly")
    logging.info(f"Travelling on a hard road, the wheels will be damaged by {damage_to_wheels}%, the drivers mood will decrease slightly")
    if max_distance >= distance:
        return True
    else:
        return False
