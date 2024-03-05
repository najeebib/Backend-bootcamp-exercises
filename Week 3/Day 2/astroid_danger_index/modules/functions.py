import json
import requests
import asyncio
from modules.astroid import Astroid
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
            astroid = Astroid(id, name, min_diameter, max_diameter, speed_kmh, miss_distance)
            list_of_astroids.append(astroid)
    return list_of_astroids

def save_astroid_to_file(list_of_astroids):
    json_list = []
    with open("astroids.json", 'w') as f:
        for astroid in list_of_astroids:
            json_list.append(astroid.get_json())
        json.dump(json_list, f, indent=2)

def calculate_danger_index(astroid, a, b, c):
    avg_diameter = (astroid.get_min_diameter() + astroid.get_max_diameter()) / 2
    danger_index = a * avg_diameter + (b * astroid.get_speed_kmh())*((1/c) * astroid.get_miss_distance()) 
    return danger_index

def plot_data(list_of_astroids, a=1, b=1, c=1):
    names = []
    danger_indices = []
    for astroid in list_of_astroids:
        names.append(astroid.get_name())
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
