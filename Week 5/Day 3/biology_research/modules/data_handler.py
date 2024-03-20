from .record import Record
from .errors import Errors
import json
class DataHandler:
    def write_to_json(self, record: Record):
        try:
            # generate a random error
            Errors.generate_write_error()
            self.write_to_file(record, './data/records.json')
        except:
            # if an error was raised, make a replica of the json file
            self.make_replica()
            # insert the record to second file
            self.write_to_file(record, './data/records2.json')
            # add the data to the first file so that it doesnt get lost
            self.merge_json_files('./data/records.json', './data/records2.json')
    def read_from_json(self):
        try:
            # generate a random error
            Errors.generate_read_error()
            return self.read_from_file('./data/records.json')
        except:
            # read from second file if an error happened
            return self.read_from_file('./data/records2.json')
    def write_to_file(self, record: Record, path):
        # write the record to a json file
        record_str = f"{record.get_timestamp()} rabbits born: {record.get_births()} rabbits died: {record.get_deaths()}"
        with open(path,'r+') as f:
            f.seek(0)
            content = f.read()
            content = json.loads(content)
            content.append(record_str)
            f.seek(0)        
            json.dump(content,f)
            f.truncate()

    def read_from_file(self, path):
        # read all records in the file
        with open(path) as f:
            Errors.generate_read_error()
            content = f.read()
            content = json.loads(content)
            return content
        
    def make_replica(self):
        # make a replica of the json file and save in it all the data that are in the first one
        with open('./data/records.json', 'r') as f:
            data = json.load(f)

        with open('./data/records2.json', 'w') as f:
            json.dump(data, f)
   
                    
    def merge_json_files(self, file1, file2):
        # load all the data from json file 1
        with open(file1, 'r') as f1:
            data1 = json.load(f1)
        # load all the data from json file 1
        with open(file2, 'r') as f2:
            data2 = json.load(f2)
        # make a list that has all the records in both files, without duplicates
        in_first = set(data1)
        in_second = set(data2)
        in_second_but_not_in_first = in_second - in_first
        result = data1 + list(in_second_but_not_in_first)
        # save all the data in the first json file
        with open(file1, 'w') as out_f:
            json.dump(result, out_f)

    # overwrite the file, this is used for deleting a record from the file, by deleting it from list then overwrite the file and put the new list
    def overwrite_file(self, records):
        with open('./data/records.json', 'w') as f:
            json.dump(records,f)

