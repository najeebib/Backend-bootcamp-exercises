import logging
from .functions import get_all_records, get_current_timestamp

def print_sum_amount(record_file: str):
    """ primt the sum of all record amounts 

        :param record_file: name of the file 
    """
    all_records = get_all_records(record_file)
    amounts = [int(record[1]) for record in all_records]
    formatted_timestamp = get_current_timestamp()
    print(f"{formatted_timestamp} PrintAmount {sum(amounts)}")
    logging.info(f"{formatted_timestamp} PrintAmount Success")

def display_records(record_file: str):
    """ print the records in order 

        :param record_file: name of the file 
    """
    all_records = get_all_records(record_file)
    sorted_list = sorted(all_records, key=lambda x: x[0])
    for record in sorted_list:
        formatted_timestamp = get_current_timestamp()
        print(f"{formatted_timestamp} PrintAll {record[0]} {record[1]}", end ="")
        logging.info(f"{formatted_timestamp} PrintAll Success")