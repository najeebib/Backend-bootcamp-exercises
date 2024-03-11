import logging

def bumpy(distance, truck):
    truck_max_fuel = truck.get_max_fuel_amount()
    truck_km_per_liter = truck.get_km_per_liter()
    # the terain hardness, the higher it is the more fule will be needed to traverse it
    road_terrain_hardness = 1.2
    max_distance = (truck_max_fuel * truck_km_per_liter) / road_terrain_hardness
    # the wheel damage, the higher it is the more damage the road will do to the wheels
    wheel_damage_effect = 0.008
    damage_to_wheels = distance * wheel_damage_effect
    
    print(f"Travelling on a bumpy road, the wheels will be damaged by {damage_to_wheels}%, the drivers mood will decrease a little bit")
    logging.info(f"Travelling on a bumpy road, the wheels will be damaged by {damage_to_wheels}%, the drivers mood will decrease a little bit")
    if max_distance >= distance:
        return True
    else:
        return False
