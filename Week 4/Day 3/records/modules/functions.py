from datetime import datetime
import logging

def get_number_from_user(upper_limit):
    """ Ask the user to enter the command number for next action

    :param upper_limit: the highest number the user can choose
    """
    while True:
        try:
            command = int(input(f"Enter the number between (1 - {upper_limit})\n"))
            if 1 <= command <= upper_limit:
                return command
            else:
                print("Enter numbers the specified range")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            logging.warning("Invalid input. Please enter a valid number.")

def add_record(record_file, name, amount):
    """ Check if the record we want to insert is in the file
        if it isn't in it, add the record to the end of the file
        otherwise print all records with similiar name and ask user which one to replace

        :param record_file: name of the file
        :param name: name of the record to be inserted
        :param name: amount of the record to be inserted
    """
    found_records = search(record_file, name)
    if len(found_records) == 0 :
        with open(record_file, 'a') as file1:
            record_str = f"{name}, {amount}\n"
            file1.write(record_str)
        print(f"Record for {name} added successfully")
    else:
        for idx, record in enumerate(found_records):
            print(f"{idx + 1}. Name: {record[0]}, Amount: {record[1]}")
        choice = get_number_from_user(len(found_records))
        record = found_records[choice - 1]
        remove_record(record_file, record[0], record[1])
        with open(record_file, 'a') as file1:
            record_str = f"{name}, {amount}\n"
            file1.write(record_str)
        print(f"Record for {name} updated successfully")
    formatted_timestamp = get_current_timestamp()
    logging.info(f"{formatted_timestamp} Insert Success")
            
def write_to_file(record_file, list):
    """ write to the file all the records in the list, add them to the end 
    
    :param record_file: name of the file
    :param list: list of records that we insert to file
    """
    with open(record_file, "a") as f:
        for record in list:
            record_str = f"{record[0]}, {record[1]}"
            f.write(record_str)

def remove_record(record_file, name, amount):
    """ check if the record exists in the file
        if it does check if there is only one, then remove it
        if there is more than one record with similar name ask user to remove one

        :param record_file: name of the file   
        :param name: name of the record we will remove 
    """
    all_records = get_all_records(record_file)
    search_list = search(record_file, name)
    if len(search_list) > 0:
        if len(search_list) == 1:
            all_records.remove(search_list[0])
            f = open(record_file, "w")
            f.close()
            write_to_file(record_file, all_records)
            formatted_timestamp = get_current_timestamp()
            logging.info(f"{formatted_timestamp} Delete Success")
        else:
            for idx, record in enumerate(search_list):
                print(f"{idx + 1}. Name: {record[0]}, Amount: {record[1]}")
            choice = get_number_from_user(len(search_list))
            record = search_list[choice]
            all_records.remove(record)
            f = open(record_file, "w")
            f.close()
            write_to_file(record_file, all_records)
            formatted_timestamp = get_current_timestamp()
            logging.info(f"{formatted_timestamp} Delete Success")
    else:
        formatted_timestamp = get_current_timestamp()
        logging.info(f"{formatted_timestamp} Delete Failure")
            
def search(record_file, name):
    """ search the file for all records with similar name as the input name

        :param record_file: name of the file 
        :param name: name of the record we want to search for
    """
    found_records = []
    with open(record_file, 'r') as file:
        for line in file:
            record_name, record_amount = line.split(", ")
            if name in record_name:
                found_records.append((record_name, record_amount))
    formatted_timestamp = get_current_timestamp()
    if len(found_records) > 0:
        logging.info(f"{formatted_timestamp} Search Success")
    else:
        logging.info(f"{formatted_timestamp} Search Failure")
    return found_records

def update_name(record_file, name, new_name):
    """ search the file for record with same name and update its name
        if there is more than one record with same name, ask user to choose which one to update, then find the index and update the record

        :param record_file: name of the file 
        :param name: name of the record we want to search for
        :param new_name: the new name
    """
    found_records = search(record_file, name)
    all_records = get_all_records(record_file)
    if len(found_records) == 1:
        idx = all_records.index(found_records[0])
        new_record = (new_name,found_records[0][1])
        all_records[idx] = new_record
        f = open(record_file, "w")
        f.close()
        write_to_file(record_file, all_records)
        formatted_timestamp = get_current_timestamp()
        logging.info(f"{formatted_timestamp} UpdateName Success")
    elif len(found_records) > 1:
        for idx, record in enumerate(found_records):
            print(f"{idx + 1}. Name: {record[0]}, Amount: {record[1]}")
        choice = get_number_from_user(len(found_records))
        record = found_records[choice - 1]
        idx = all_records.index(record)
        new_record = (new_name,record[1])
        all_records[idx] = new_record
        f = open(record_file, "w")
        f.close()
        write_to_file(record_file, all_records)
        formatted_timestamp = get_current_timestamp()
        logging.info(f"{formatted_timestamp} UpdateName Success")
    else:
        formatted_timestamp = get_current_timestamp()
        logging.info(f"{formatted_timestamp} UpdateName Failure")
    
def update_amount(record_file, name, new_amount):
    """ search the file for record with same name and update its amount
        if there is more than one record with same name, ask user to choose which one to update, then find the index and update the record

        :param record_file: name of the file 
        :param name: name of the record we want to search for
        :param new_amount: the new amount
    """
    found_records = search(record_file, name)
    all_records = get_all_records(record_file)
    if len(found_records) == 1:
        idx = all_records.index(found_records[0])
        new_record = (found_records[0][0],new_amount)
        all_records[idx] = new_record
        write_to_file(record_file, all_records)
        formatted_timestamp = get_current_timestamp()
        logging.info(f"{formatted_timestamp} UpdateAmount Success")
    elif len(found_records) > 1  :
        for idx, record in enumerate(found_records):
            print(f"{idx + 1}. Name: {record[0]}, Amount: {record[1]}")
        choice = get_number_from_user(len(found_records))
        record = found_records[choice - 1]
        idx = all_records.index(record)
        new_record = (record[0],new_amount)
        all_records[idx] = new_record
        write_to_file(record_file, all_records)
        formatted_timestamp = get_current_timestamp()
        logging.info(f"{formatted_timestamp} UpdateAmount Success")
    else:
        formatted_timestamp = get_current_timestamp()
        logging.info(f"{formatted_timestamp} UpdateAmount Failure")
        

def get_all_records(record_file):
    """ get all the records in a list """
    records = []
    with open(record_file, "r") as f:
        for record in f.readlines():
            record_name, record_amount = record.split(", ")
            records.append((record_name, record_amount))
    return records

def get_current_timestamp():
    """ get the current datetime """
    curent_timestamp = datetime.now()
    formatted_timestamp = curent_timestamp.strftime("%d/%m/%Y %H:%M:%S")
    return formatted_timestamp

def print_sum_amount(record_file):
    """ primt the sum of all record amounts 

        :param record_file: name of the file 
    """
    all_records = get_all_records(record_file)
    amounts = [int(record[1]) for record in all_records]
    formatted_timestamp = get_current_timestamp()
    print(f"{formatted_timestamp} PrintAmount {sum(amounts)}", end ="")
    logging.info(f"{formatted_timestamp} PrintAmount Success")

def display_records(record_file):
    """ print the records in order 

        :param record_file: name of the file 
    """
    all_records = get_all_records(record_file)
    sorted_list = sorted(all_records, key=lambda x: x[0])
    for record in sorted_list:
        formatted_timestamp = get_current_timestamp()
        print(f"{formatted_timestamp} PrintAll {record[0]} {record[1]}", end ="")
        logging.info(f"{formatted_timestamp} PrintAll Success")