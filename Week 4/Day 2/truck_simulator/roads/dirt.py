import logging

def dirt(distance, truck):
    truck_max_fuel = truck.get_max_fuel_amount()
    truck_km_per_liter = truck.get_km_per_liter()
    road_terrain_hardness = 2
    max_distance = (truck_max_fuel * truck_km_per_liter) / road_terrain_hardness
    wheel_damage_effect = 0.012
    damage_to_wheels = distance * wheel_damage_effect
    print(f"Travelling on a dirt road, the wheels will be damaged by {damage_to_wheels}%, the drivers mood will decrease a lot")
    logging.info(f"Travelling on a dirt road, the wheels will be damaged by {damage_to_wheels}%, the drivers mood will decrease a lot")

    if max_distance >= distance:
        return True
    else:
        return False
    
