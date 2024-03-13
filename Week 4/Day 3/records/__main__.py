from modules.functions import search, get_number_from_user, get_current_timestamp
from modules.add_remove import add_record, remove_record
from modules.records_print import print_sum_amount, display_records
from modules.records_update import update_amount, update_name
import sys
import logging


def get_amount_from_user():
    """ Ask the user to enter the amount """
    while True:
        try:
            amount= int(input(f"Enter the amount: "))
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            logging.warning("Invalid input. Please enter a valid number.")
    
def main():
    file_name = "record_files/"+sys.argv[1] + ".txt"
    logging.basicConfig(level=logging.INFO, filename="log_files/"+sys.argv[1]+"_log.log", filemode="w")
    f = open(file_name, 'a+')
    f.close()
    while True:
        command = get_number_from_user(8)
        match command:
            case 1:
                name = input("Enter name of the record: ")
                amount = get_amount_from_user()
                add_record(file_name, name, amount)
            case 2:
                name = input("Enter name of the record to delete: ")
                amount = get_amount_from_user()
                remove_record(file_name, name, amount)
                
            case 3:
                name = input("Enter name of the record to search: ")
                result = search(file_name, name)
                print(result)
                
            case 4:
                name = input("Enter name of the record: ")
                new_name = input("Enter new name of the record: ")
                update_name(file_name, name, new_name)
            case 5:
                name = input("Enter the name of the record to update its amount: ")
                new_amount = get_amount_from_user()
                update_amount(file_name, name, new_amount)
            case 6:
                print_sum_amount(file_name)
            case 7:
                display_records(file_name)
                
            case 8:
                formatted_timestamp = get_current_timestamp()
                logging.info(f"{formatted_timestamp} Exit Success")
                break



if __name__ == "__main__":
    main()