def get_user_input():
    # ask the user for the task info
    task_name = input("Enter task name\n")
    duration_str = input("Enter task duration (from 1 to 8)\n")
    duration = 0
    if duration_str.isnumeric():
        duration = int(duration_str)
    else:
        print("wrong type, enter a number pleas")
    day_str = input("Enter specific day (1 - 5) (optional)\n")
    day = -1
    if day_str != "":
        day = int(day_str)
    hour_str = input("Enter specific hour (1 - 8) (optional)\n")
    hour = -1
    if hour_str != "":
        hour = int(hour_str)
    return task_name, duration, day, hour
# go through all  the callendar and check if there is a free space for the task
def check_day_has_time(scheduler, day_index, hour_index):
    is_available = True
    for i in range(hour_index, hour_index + duration):
        if i < 8:
            if scheduler[day_index][i] != None:
                is_available = False
                break
    return is_available
# insert task to calendar
def insert_task(scheduler, day_index, hour_index):
    for i in range(hour_index, hour_index + duration):
            if i < 8:
                scheduler[day_index][i] = task_name
# return the task index in the calendar 
def get_task_location(scheduler, duration):
    day_index = -1
    hour_index = -1
    for i in range(5):
        count = 0
        final_hour = 0
        for j in range(8):
            if scheduler[i][j] == None and count != duration:
                count +=1
                final_hour = j
        if count == duration:
            day_index = i
            hour_index = final_hour + 1 - duration
            break
    return day_index, hour_index
# print all tasks in the calendar
def print_all_tasks(scheduler):
    for i in range(5):
        for j in range(8):
            if scheduler[i][j] != None:
                print(f"Day: {i} Hour: {j}, task: {scheduler[i][j]}")

scheduler = [[None] * 8 for _ in range(5)]
keep_going = True
while keep_going:
    # ask user to enter action command
    user_input = input("Enter a number a number for what action do you want to be done:\n1. Enter new task\n2. close\n")
    if user_input.isnumeric():
        command = int(user_input)
        match command:
            case 1:
                task_name, duration, day, hour = get_user_input()
                if hour != -1 and day != -1:
                    day_index = day -1
                    hour_index = hour - 1
                    is_available = check_day_has_time(scheduler, day_index, hour_index)
                    
                    if is_available:
                        insert_task(scheduler, day_index, hour_index)
                    else:
                        for i in range(hour_index, hour_index + duration):
                            if i < 8:
                                if scheduler[day_index][i] != None:
                                    print(f"Hour: {i}, task: {scheduler[day_index][i]}")
                        replcae_str = input("This date isn't available, do you want to replace it with new task? (type y/n)")
                        if replcae_str == "y":
                            insert_task(scheduler, day_index, hour_index) 
                else:
                    day_index, hour_index =  get_task_location(scheduler, duration)
                    if day_index != -1 and hour_index != -1:
                        insert_task(scheduler, day_index, hour_index)   
                    else:
                        print("there is no time available for this task") 
                print("task was added")
            case 2:
                print_all_tasks(scheduler)
                keep_going = False

