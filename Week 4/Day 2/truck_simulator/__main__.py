from modules.truck import Truck
from modules.read_data import read_roads_file 
from traversal_calculator import Traversal_calculator
import logging

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")

def main():
    truck = Truck(20, 50,200,"Toyota")
    calc = Traversal_calculator()
    

    roads = read_roads_file("data/roads.json")
    for road in roads:
        print(calc.can_travel(truck, road["length"], road["road_type"]))

if __name__ == "__main__":
    main()