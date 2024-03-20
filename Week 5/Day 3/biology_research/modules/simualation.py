import time
import random
from .data_handler import DataHandler
from .record import Record
from datetime import datetime

class Simulation:
    def __init__(self):
        self._rabbits_num = 100
        self._num_of_inserted_records = 0
        self._max_num_records = random.randint(100,300)
    
    def get_rabbits_num(self):
        return self._rabbits_num
    
    def add_rabbits_num(self, number):
        self._rabbits_num += number

    def get_inserted(self):
        return self._num_of_inserted_records
    
    def increment_inserted(self):
        self._num_of_inserted_records += 1

    def simulation(self):
        data_handler = DataHandler()
        count = 0
        max_records = self._max_num_records
        while self._num_of_inserted_records < max_records:
            # initilize a new record
            timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            deaths_num = random.randint(0, 20)
            births_num = random.randint(0, 25)
            record = Record(timestamp, deaths_num, births_num)
            # insert the record to json file
            data_handler.write_to_json(record)
            self.increment_inserted()
            delay = random.randint(5,10)
            time.sleep(delay)
            if count == 10:
                # analyze the records, check if deaths are not bigger that total number of rabbit, delete if it is
                count = 0
                records = data_handler.read_from_json()
                change = 0
                has_invalid_records = False
                for record in records[-10:]:
                    line_split = record.split()
                    change += int(line_split[4]) - int(line_split[7])
                    if self._rabbits_num < record.get_deaths():
                        has_invalid_records = True
                        records.remove(record)
                        print("A record has been removed")
                    else:
                        change += record.get_births() - record.get_deaths()
                if has_invalid_records:
                    data_handler.overwrite_file(records)
                self._rabbits_num += change
                print(f"There are {self._rabbits_num} rabbits")
            else:
                count += 1
