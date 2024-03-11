from modules.truck import Truck
from modules.read_data import read_roads_file 
from traversal_calculator import Traversal_calculator
import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")

def main():
    # init a truck
    truck = Truck(20, 50,200,"Toyota")
    # init a traversal calculator
    calc = Traversal_calculator()
    
    # read the roads fro json file
    roads = read_roads_file("data/roads.json")
    for road in roads:
        if calc.can_travel(truck, road["length"], road["road_type"]):
            name = truck.get_brand()
            print(f"Truck brand: {name} can travel the {road['road_type']} road with length {road['length']} KM")
        else:
             print(f"Truck brand: {name} can't travel the {road['road_type']} road with length {road['length']} KM")

if __name__ == "__main__":
    main()