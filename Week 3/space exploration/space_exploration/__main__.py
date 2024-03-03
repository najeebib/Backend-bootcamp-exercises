import random
import time
import math
import json
import requests
from space_exploration.spaceship import SpaceShip
def convert_to_num(str):
    if str.isnumeric():
        return int(str)
    return -1

keep_going = True
launch = False
spaceship = SpaceShip("Rocinante", 100, 100)
while keep_going:
    if not launch:
        user_input = input("Enter what do you want to do\n1. Launch space ship\n2. Close the game\n")
        command = convert_to_num(user_input)
        match command:
            case 1:
                print("The space ship has been launched")
                launch = True
            case 2:
                keep_going = False
            case _:
                print("Enter valid input")
    else:
        time.sleep(2)
        chance = random.random()
        if chance < 0.5:
            print(spaceship)
            valid = False
            while not valid:
                action_str = input("Enter what do you want to do\n1. Keep exploring\n2. Return home\n")
                action = convert_to_num(action_str)
                if action == 1:
                    valid = True
                elif action == 2:
                    print("Space ship is en route to home planet")
                    valid = True
                    keep_going = False
                else:
                    print("Enter valid action")
        elif chance > 0.5 and chance < 0.625:
            valid = False
            while not valid:
                action_str = input("Enter what do you want to do\n1. Try to evade the field\n2. Fire at the field\n")
                action = convert_to_num(action_str)
                if action == 1:
                    valid = True
                    print("space shipe evaded the field")
                elif action == 2:
                    print("space ship fired at the field")
                    valid = True
                else:
                    print("Enter valid action")
        elif chance > 0.625 and chance < 0.75:
            print("pirates")
        elif chance > 0.75 and chance < 0.875:
            print("alien")
        else:
            print("black hole")