from modules.truck import Truck
from traversal_calculator import Traversal_calculator
def main():
    truck = Truck(20, 50,200,"Toyota")
    calc = Traversal_calculator()
    # todo: get roads from json file, for now use hardcoded values to test if code works
    print(calc.can_travel(truck, 700, "hard"))
    print(calc.can_travel(truck, 500, "hard"))


if __name__ == "__main__":
    main()