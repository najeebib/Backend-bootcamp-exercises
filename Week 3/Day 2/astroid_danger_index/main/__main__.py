from dotenv import load_dotenv
import os
from datetime import date
import asyncio
import requests
import json
import matplotlib.pyplot  as plt
async def get_data(url):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, url)
    response = await  future
    string = response.text
    json_obj = json.loads(string)

    return json_obj

def save_astroid_list(all_astroids):
    list_of_astroids = []
    for key, value in all_astroids.items():
        for astroid in value:
            id = astroid["id"]
            name = astroid["name"]
            min_diameter = float(astroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"])
            max_diameter = float(astroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"])
            close_approach_data = astroid["close_approach_data"][0]
            speed_kmh = float(close_approach_data["relative_velocity"]["kilometers_per_hour"])
            miss_distance = float(close_approach_data["miss_distance"]["kilometers"])
            json_object = {"id": id ,"name": name, "min_diameter": min_diameter, "max_diameter": max_diameter, "miss_distance": miss_distance, "speed_kmh": speed_kmh}
            list_of_astroids.append(json_object)
    return list_of_astroids

def save_astroid_to_file(list_of_astroids):
    with open("astroids.json", 'w') as f:
        json.dump(list_of_astroids, f, indent=2)

def calculate_danger_index(astroid, a, b, c):
    avg_diameter = (astroid["min_diameter"] + astroid["max_diameter"]) / 2
    danger_index = a * avg_diameter + (b * astroid["speed_kmh"])*((1/c) * astroid["miss_distance"]) 
    return danger_index

def plot_data(list_of_astroids, a=1, b=1, c=1):
    names = []
    danger_indices = []
    for astroid in list_of_astroids:
        names.append(astroid["name"])
        danger_index = calculate_danger_index(astroid, a, b, c)
        danger_indices.append(danger_index)

    plt.figure(figsize=(10, 5))
    plt.bar(names, danger_indices)
    plt.xlabel("Asteroid Names")
    plt.ylabel("Danger Index")
    plt.title("Asteroid Danger Index")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


load_dotenv()
api_key = os.getenv("API_KEY")

current_date = date.today()
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={current_date}&api_key={api_key}"

loop = asyncio.get_event_loop()
data = loop.run_until_complete(get_data(url))
all_astroids = data["near_earth_objects"]

list_of_astroids = save_astroid_list(all_astroids)
save_astroid_to_file(list_of_astroids)
valid = False
keep_asking_for_input = True
while keep_asking_for_input:
    user_input = input("Do you want to enter the A, B, C coefficents? (y/n)\n")
    if user_input == 'y':
        valid = True
        a = 1
        b = 1
        c = 1
        a_str = input("Enter A (must be an integer)\n")
        if a_str.isnumeric():
            a = int(a_str)
        b_str = input("Enter B (must be an integer)\n")
        if a_str.isnumeric():
            b = int(b_str)
        c_str = input("Enter C (must be an integer)\n")
        if c_str.isnumeric():
            c = int(c_str)
        plot_data(list_of_astroids, a, b, c)
    elif user_input == 'n':
        valid = True
        plot_data(list_of_astroids)
    else:
        print("Enter y or n")
    keep_going = input("Do you want to close program? (y/n)\n")
    if keep_going == 'y':
        keep_asking_for_input = False



