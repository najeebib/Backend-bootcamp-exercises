from datetime import datetime
import logging

def get_number_from_user(upper_limit: int):
    """ Ask the user to enter the command number for next action

    :param upper_limit: the highest number the user can choose
    """
    while True:
        try:
            command = int(input(f"Enter the number between (1 - {upper_limit}).\n1. Add record.\n2. Remove record.\n3. Search record.\n4. Update record name.\n5. Update record amount.\n6. Print records amount sum.\n7. Print recors.\n8. Exit.\n"))
            if 1 <= command <= upper_limit:
                return command
            else:
                print("Enter numbers the specified range")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            logging.warning("Invalid input. Please enter a valid number.")
        
def write_to_file(record_file: str, list: list):
    """ write to the file all the records in the list, add them to the end 
    
    :param record_file: name of the file
    :param list: list of records that we insert to file
    """
    with open(record_file, "a") as f:
        for record in list:
            record_str = f"{record[0]}, {record[1]}"
            f.write(record_str)

            
def search(record_file: str, name: str):
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


def get_all_records(record_file: str):
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