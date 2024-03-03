import random
import time
import math
import json
import requests
import os

from space_exploration.spaceship import SpaceShip
# todo: refractor the code, make it cleaner, split to more functions and classes maybe?
def convert_to_num(str):
    if str.isnumeric():
        return int(str)
    return -1

def save_ship_json(spaceship):
    name = spaceship.get_name()
    fuel = spaceship.get_fuel()
    health = spaceship.get_health()
    ship_data = {"name": name, "fuel": fuel, "health": health}
    with open("ship.json", "w") as json_file:
        json.dump(ship_data, json_file)
        print("Spaceship data saved to ship.json.")

def read_ship_data(file_name):
    with open(file_name, "r") as json_file:
        try:
            ship_data = json.load(json_file)
            return ship_data
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file '{file_name}'.")
            return None

request_endpoint = "https://api.open-meteo.com/v1/forecast?latitude=32.689516&longitude=35.373868&current=temperature_2m"
keep_going = True
launch = False
name = ""
fuel = 100
health = 100

if os.path.exists("ship.json"):
    new_ship = input("Do you want to send a new ship or use the previous one\n1. New one\n2. Use old one\n")
    command = convert_to_num(new_ship)
    if command == 2:
        data = read_ship_data("ship.json")
        if data:
            name = data["name"]
            fuel = data["fuel"]
            health = data["health"]
    else:
        name = input("Enter ship name\n")
spaceship = SpaceShip(name, fuel, health)

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
        fuel = spaceship.get_fuel()
        health = spaceship.get_health()
        time.sleep(2)
        chance = random.random()
        if chance < 0.5:
            
            valid = False
            while not valid:
                action_str = input("Enter what do you want to do\n1. Keep exploring\n2. Return home\n")
                action = convert_to_num(action_str)
                if action == 1:
                    valid = True
                    r = requests.get(request_endpoint)
                    data = r.json()
                    current_temperature = data["current"]["temperature_2m"]
                    print(f"Temperature at current location is {current_temperature}")

                elif action == 2:
                    print("Space ship is en route to home planet")
                    save_ship_json(spaceship)
                    valid = True
                    keep_going = False
                else:
                    print("Enter valid action")
        elif chance > 0.5 and chance < 0.625:
            print("You encountered an astroid field")
            valid = False
            while not valid:
                action_str = input("Enter what do you want to do\n1. Try to evade the field\n2. Fire at the field\n")
                action = convert_to_num(action_str)
                if action == 1:
                    health -= random.randint(5,18)
                    valid = True
                    print("space shipe evaded the field but has sustained some damage")
                elif action == 2:
                    
                    health -= random.randint(5,12)
                    print("space ship fired at the field, you were able to destroy some meteors but not all")
                    
                    valid = True
                else:
                    print("Enter valid action")
            spaceship.set_health(health)
        elif chance > 0.625 and chance < 0.75:
            print("You encountered a pirate ship")
            valid = False
            while not valid:
                action_str = input("Enter what do you want to do\n1. Fight the pirates\n2. Try to evade the enemy ship\n")
                action = convert_to_num(action_str)
                if action == 1:
                    health -= random.randint(12,25)
                    valid = True
                    print("You managed to destroy the enemy ship, but sustained heavy damage")
                elif action == 2:
                    health -= random.randint(10,18)
                    print("You escaped the enemy ship, but sustained some dam age during retreat")
                    valid = True
                else:
                    print("Enter valid action")
            spaceship.set_health(health)
        elif chance > 0.75 and chance < 0.875:
            print("You encountered an alien ship")
            valid = False
            while not valid:
                action_str = input("Enter what do you want to do\n1. Attack the alien ship\n2. Negotiate with the aliens\n")
                action = convert_to_num(action_str)
                if action == 1:
                    health -= random.randint(12,30)
                    valid = True
                    print("You managed to destroy the enemy ship, but sustained heavy damage")
                elif action == 2:
                    print("You successfully negotiated with the alien ship")
                    valid = True
                else:
                    print("Enter valid action")
            spaceship.set_health(health)
        else:
            print("You encountered a black hole")
            valid = False
            while not valid:
                action_str = input("Enter what do you want to do\n1. Try to escape\n2. Accept death\n")
                action = convert_to_num(action_str)
                if action == 1:
                    odds = random.random()
                    if odds < 0.5:
                        print("You escaped the black hole but suffered havy damage")
                        health -= random.randint(24, 38)
                        spaceship.set_health(health)
                    else:
                        spaceship.set_health(0)
                        print("You got pulled into the black hole and died")
                        keep_going = False
                    valid = True
                    print("You managed to destroy the enemy ship, but sustained heavy damage")
                elif action == 2:
                    spaceship.set_health(0)
                    print("You got pulled into the black hole and died")
                    keep_going = False
                else:
                    print("Enter valid action")
            
        fuel -= random.randint(5,12)
        spaceship.set_fuel(fuel)
        if fuel < 1:
            print("Ship ran out of fuel, you are stuck in space till death")
            keep_going = False
        if health < 1:
            print("Your ship has been destroyed")
            keep_going = False
        print(spaceship)