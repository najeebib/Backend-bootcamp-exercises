import os
import re
from datetime import datetime, timedelta

def read_all_records(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line)

def get_last_record(file_name):
    last = ""
    with open(file_name, 'r') as f:
        for line in f.readlines():
            last = line
    return last
def print_range(file_name, from_str, to_str, date_pattern):
    date_format = "%d-%m-%Y"
    from_date = datetime.strptime(from_str, date_format)
    to_date = datetime.strptime(to_str, date_format)
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line_date_str = find_date(line,date_pattern)
            line_date = datetime.strptime(line_date_str, date_format)
            if from_date < line_date < to_date:
                print(line)
                
def find_date(entry, date_pattern):
    date_str = ""
    date_match = re.search(date_pattern, entry)
    if date_match:
        date_str = date_match.group()
    return date_str
def is_same_week(mood_str, last_record, date_pattern):

    mood_date_str = find_date(mood_str, date_pattern)
    last_record_date_str = find_date(last_record, date_pattern)

    date_format = "%d-%m-%Y"
    try:
        mood_date = datetime.strptime(mood_date_str, date_format)
        last_record_date = datetime.strptime(last_record_date_str, date_format)

        week_start_mood = mood_date - timedelta(days=mood_date.weekday())
        week_start_last = last_record_date - timedelta(days=last_record_date.weekday())
        return week_start_mood == week_start_last

    except ValueError:
        print("Invalid date format. Please provide the date in the format:", date_format)
        
emotions_dictionary = {"Joy":["happy","excited","delighted","blissful","jubilant"], "Sadness":["unhappy","depressed","sorrowful","mournful","melancholic"]
                       ,"Anger":["furious","irritated","enraged","annoyed","agitated"], "Fear":["scared","terrified","anxious","nervous","panicked"]
                       ,"Surprise":["astonished","amazed","startled","shocked","stunned"], "Disgust":["repulsed","revolted","displeased","sickend","appalled"]
                       ,"Love":["affectionate","adoring","fond","devoted","enamored"], "Confusion":["bewildered","perplexed","baffled","confused","puzzled"]
                       ,"Contentment":["satisfied","pleased","gratified","content","fullfilled"], "Embarrassment":["ashamed","humiliated","blushing","self-conscious","mortified"]}
datetime_pattern = r'^\d{2}:\d{2}-\d{2}-\d{2}-\d{4}$'
date_pattern = r'\d{2}-\d{2}-\d{4}$'

name = input("Enter your name \n")
file_name = name + ".txt"

mood_string =  input("Enter your current mood\n")
date_match  = re.search(date_pattern, mood_string)
if date_match:
    mood_string += "\n"
else:
    now = datetime.now()
    dt_string = now.strftime("%H:%M-%d-%m-%Y")
    mood_string = mood_string + " " + dt_string + "\n"
last_record = get_last_record(file_name)
if is_same_week(mood_string, last_record, date_pattern):
    print("new entry is in same week as last one")
else:
    print("new entry isn't in same week as last one")
with open(file_name, 'a+') as f:
    f.write(mood_string)
