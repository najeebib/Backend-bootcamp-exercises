from .record import Record
from .errors import Errors
import json
class DataHandler:
    def write_to_file(record: Record):
        record_str = f"{record.get_timestamp()} rabbits born: {record.get_births()} rabbits died: {record.get_deaths()}.\n"
        with open('./data/records.json','r+') as f:
            f.seek(0)
            content = f.read()
            content = json.loads(content)
            content.append(record_str)
            f.seek(0)        
            json.dump(content,f)
            f.truncate()

    def read_from_file():
        with open('./data/records.json') as f:
            Errors.generate_read_error()
            content = f.read()
            content = json.loads(content)
            return content[-10:]
        return 