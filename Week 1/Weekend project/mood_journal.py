import os
import re
from datetime import datetime

pattern_str = r'^\d{2}:\d{2}-\d{2}-\d{2}-\d{4}$'
 
name = input("Enter your name \n")
file_name = name + ".txt"

mood_string =  input("Enter your current mood\n")
date_str = mood_string[-16::1]
print(date_str)
print(re.match(pattern_str, date_str))
if re.match(pattern_str, date_str):
    print(date_str)
    mood_string += "\n"
    with open(file_name, 'a+') as f:
        f.write(mood_string)
else:
    now = datetime.now()
    dt_string = now.strftime("%H:%M-%d-%m-%Y")
    mood_string = mood_string + " " + dt_string + "\n"
    with open(file_name, 'a+') as f:
        f.write(mood_string)


