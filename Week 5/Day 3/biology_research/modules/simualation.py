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
        count = 0
        max_records = self._max_num_records
        while self._num_of_inserted_records < max_records:
            timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            deaths_num = random.randint(0, 20)
            births_num = random.randint(0, 25)
            record = Record(timestamp, deaths_num, births_num)
            DataHandler.write_to_file(record)
            self.increment_inserted()
            delay = random.randint(5,10)
            time.sleep(delay)
            if count == 10:
                count = 0
                print(DataHandler.read_from_file())
            else:
                count += 1
