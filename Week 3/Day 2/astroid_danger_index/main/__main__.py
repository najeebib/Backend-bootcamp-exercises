from dotenv import load_dotenv
import os
from datetime import date
import asyncio
from modules.functions import save_astroid_list, save_astroid_to_file, get_data, plot_data 
# lod the API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")
# construct the API endpoint
current_date = date.today()
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={current_date}&api_key={api_key}"
# get the data
loop = asyncio.get_event_loop()
data = loop.run_until_complete(get_data(url))
all_astroids = data["near_earth_objects"]
# save the data in a list and a file
list_of_astroids = save_astroid_list(all_astroids)
save_astroid_to_file(list_of_astroids)
# check if the user input is valid
valid = False
keep_asking_for_input = True
# ask the user for the input
while keep_asking_for_input:
    user_input = input("Do you want to enter the A, B, C coefficents? (y/n)\n")
    # if the user want to enter the coefficents
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