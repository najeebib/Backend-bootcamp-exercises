import logging
from .functions import search, get_all_records, get_current_timestamp, get_number_from_user, write_to_file

def update_name(record_file: str, name: str, new_name: str):
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
            print(f"{idx + 1}. Name: {record[0]}, Amount: {record[1]}", end ="")
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
    
def update_amount(record_file: str, name: str, new_amount: int):
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
            print(f"{idx + 1}. Name: {record[0]}, Amount: {record[1]}", end ="")
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
