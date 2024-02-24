import os
import re
from datetime import datetime, timedelta
from bisect import bisect_left

def read_records(file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            for line in f.readlines():
                print(line)

def get_all_records(file_name, datetime_pattern):
    dates = []
    records = []
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            for line in f.readlines():
                date_str = find_date(line, datetime_pattern)
                date_format = "%H:%M-%d-%m-%Y"
                date = datetime.strptime(date_str, date_format)
                index_to_insert = bisect_left(dates, date)
                dates.insert(index_to_insert, date)
                records.insert(index_to_insert, line)
    return dates, records
    
def ordered_insert(file_name,dates, records, datetime_pattern, mood_entry):
    date_str = find_date(mood_entry, datetime_pattern)
    date_format = "%H:%M-%d-%m-%Y"
    date = datetime.strptime(date_str, date_format)
    index = -1
    dates_size = len(dates)
    is_between = False
    for i in range(dates_size-1):
        if dates[i] < date and dates[i+1] > date:
            index = i
            is_between = True
            break
    
    if not is_between:
        index = dates_size+1
    records.insert(index+1, mood_entry)
    with open(file_name, 'w') as f:
        for line in records:
            f.write(line)

def get_last_record(file_name):
    last = ""
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            for line in f.readlines():
                last = line
    return last

def print_range(file_name, from_str, to_str, datetime_pattern):
    date_format = "%d-%m-%Y"
    from_date = datetime.strptime(from_str, date_format)
    to_date = datetime.strptime(to_str, date_format)
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line_date_str = find_date(line,datetime_pattern)
                line_date = datetime.strptime(line_date_str, date_format)
                if from_date < line_date < to_date:
                    print(line)

def delete_range(file_name, from_str, to_str, datetime_pattern):
    dates, records = get_all_records(file_name, datetime_pattern)
    date_format = "%d-%m-%Y"
    from_date = datetime.strptime(from_str, date_format)
    to_date = datetime.strptime(to_str, date_format)
    indices_to_remove = [i for i, date in enumerate(dates) if from_date <= date <= to_date]
    for index in indices_to_remove:
        del dates[index]
        del records[index]
    with open(file_name, 'w') as f:
        for line in records:
            f.write(line)

def find_date(entry, datetime_pattern):
    date_str = ""
    date_match = re.search(datetime_pattern, entry)
    if date_match:
        date_str = date_match.group()
    return date_str
def is_same_week(mood_str, last_record, datetime_pattern):
    mood_date_str = find_date(mood_str, datetime_pattern)
    last_record_date_str = find_date(last_record, datetime_pattern)
    date_format = "%d-%m-%Y"
    try:
        mood_date = datetime.strptime(mood_date_str, date_format)
        last_record_date = datetime.strptime(last_record_date_str, date_format)

        week_start_mood = mood_date - timedelta(days=mood_date.weekday())
        week_start_last = last_record_date - timedelta(days=last_record_date.weekday())
        return week_start_mood == week_start_last

    except ValueError:
        print("Invalid date format. Please provide the date in the format:", date_format)

def is_after(mood_str, last_record, datetime_pattern):
    mood_date_str = find_date(mood_str, datetime_pattern)
    last_record_date_str = find_date(last_record, datetime_pattern)
    date_format = "%d-%m-%Y"
    try:
        mood_date = datetime.strptime(mood_date_str, date_format)
        last_record_date = datetime.strptime(last_record_date_str, date_format)
        date_difference = mood_date - last_record_date
        return date_difference >= timedelta(days=1)

    except ValueError:
        print("Invalid date format. Please provide the date in the format:", date_format)
def get_day_records(file_name, last_record_date):
    records = []
    date_format = "%d-%m-%Y"
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line_date_str = find_date(line, r'\d{2}-\d{2}-\d{4}$')
                line_date = datetime.strptime(line_date_str, date_format)
                if line_date == last_record_date:
                    records.append(line)
    return records

def check_day_emotions(emotions_count, records, emotions_dictionary):
    total = 0
    for record in records:
        emotion = check_emotion(record, emotions_dictionary)
        if emotion != None:
            emotions_count[emotion] += 1
            total += 1
    return emotions_count, total

def check_emotion(entry, emotions_dictionary):
    for key in emotions_dictionary:
        words = emotions_dictionary[key]
        for word in words:
            index = entry.lower().find(word)
            if index != -1:
                return key
    return None

emotions_dictionary = {"Joy":["happy","excited","delighted","blissful","jubilant"], "Sadness":["unhappy","depressed","sorrowful","mournful","melancholic"]
                       ,"Anger":["furious","irritated","enraged","annoyed","agitated"], "Fear":["scared","terrified","anxious","nervous","panicked"]
                       ,"Surprise":["astonished","amazed","startled","shocked","stunned"], "Disgust":["repulsed","revolted","displeased","sickend","appalled"]
                       ,"Love":["affectionate","adoring","fond","devoted","enamored"], "Confusion":["bewildered","perplexed","baffled","confused","puzzled"]
                       ,"Contentment":["satisfied","pleased","gratified","content","fullfilled"], "Embarrassment":["ashamed","humiliated","blushing","self-conscious","mortified"]}
datetime_pattern = r'\d{2}:\d{2}-\d{2}-\d{2}-\d{4}$'
date_pattern = r'\d{2}-\d{2}-\d{4}$'


name = input("Enter your name \n")
file_name = name + ".txt"

keep_going = True
while keep_going:
    user_input = input("Enter a number a number for what action do you want to be done:\n1. Enter new mood entry\n2. Print all records\n3. Print records in range (date format dd-mm-yyyy dd-mm-yyyy)\n4. Delete records in range\n5. Exit\n")
    if user_input.isnumeric():
        command = int(user_input)
        match command:
            case 1:
                

                mood_string =  input("Enter your current mood\n")
                date_match  = re.search(date_pattern, mood_string)
                if date_match:
                    mood_string += "\n"
                else:
                    now = datetime.now()
                    dt_string = now.strftime("%H:%M-%d-%m-%Y")
                    mood_string = mood_string + " " + dt_string + "\n"

                if os.path.isfile(file_name):
                    last_record = get_last_record(file_name)
                    dates, records = get_all_records(file_name, datetime_pattern)
                    if is_same_week(mood_string, last_record, date_pattern):
                        print("new entry is in same week as last one")
                    else:
                        print("new entry isn't in same week as last one")
                    if is_after(mood_string, last_record, date_pattern):
                        last_record_date_str = find_date(last_record, date_pattern)
                        date_format = "%d-%m-%Y"
                        last_record_date = datetime.strptime(last_record_date_str, date_format)
                        emotions_count = {"Joy": 0,"Sadness": 0,"Anger": 0,"Fear": 0,"Surprise": 0,"Disgust": 0,"Love": 0,"Confusion": 0,"Contentment": 0,"fullfilled": 0}
                        day_records = get_day_records(file_name, last_record_date)
                        emotions_count, total = check_day_emotions(emotions_count, day_records, emotions_dictionary)
                        day_report = f"last day you were "
                        for key in emotions_count:
                            if emotions_count[key] > 0:
                                percent = (emotions_count[key] / total) * 100
                                day_report += f" {percent}% {key} "
                        print(day_report)
                    ordered_insert(file_name, dates, records, datetime_pattern, mood_string)
                else:
                    with open(file_name, 'w+') as f:
                        f.write(mood_string)
            case 2:
                read_records(file_name)
            case 3:
                date_range = input("Enter range (from to) (dd-mm-yyyy dd-mm-yyyy)\n").split()
                print_range(file_name, date_range[0], date_range[1], date_pattern)
            case 4:
                date_range = input("Enter range (from to) (dd-mm-yyyy dd-mm-yyyy)\n").split()
                delete_range(file_name, date_range[0], date_range[1], date_pattern)
            case 5:
                keep_going = False
