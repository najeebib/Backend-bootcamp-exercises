import logging
from .functions import search, get_all_records, get_current_timestamp, get_number_from_user, write_to_file

def add_record(record_file: str, name: str, amount: int):
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
            print(f"{idx + 1}. Name: {record[0]}, Amount: {record[1]}", end ="")
        choice = get_number_from_user(len(found_records))
        record = found_records[choice - 1]
        remove_record(record_file, record[0], record[1])
        with open(record_file, 'a') as file1:
            record_str = f"{name}, {amount}\n"
            file1.write(record_str)
        print(f"Record for {name} updated successfully")
    formatted_timestamp = get_current_timestamp()
    logging.info(f"{formatted_timestamp} Insert Success")

def remove_record(record_file: str, name:str, amount: int):
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
