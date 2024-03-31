import json
from .student import Student 
""" a class to handle the data from json file """
class DataHandler:
    def __init__(self):
        self.path = "./data/students.json"
    # read the data from the json file
    def get_students(self):
        with open(self.path, "r") as f:
            content = f.read()
            content = json.loads(content)
            return content
    # add a new student to json file
    def add_student(self, student: Student):
        # make a json object of the student
        student_dict = {"name":student.get_name(), "id": student.get_id(), "age":  student.get_age(), "classes": student.get_classes()}
        with open(self.path,'r+') as f:
            f.seek(0)
            content = f.read()
            content = json.loads(content)
            # add new student to json 
            content.append(student_dict)
            f.seek(0)        
            json.dump(content,f, indent=2)
            f.truncate()