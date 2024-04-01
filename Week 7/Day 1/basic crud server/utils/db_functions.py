import json
from modules.student import Student


# read the data from the json file
def load_db(path):
    with open(path, "r") as f:
        content = f.read()
        content = json.loads(content)
        return content
# add a new student to json file
def add_student(student: Student, path='./data/students.json'):
    # make a json object of the student
    student_dict = {"name":student.get_name(), "id": student.get_id(), "age":  student.get_age(), "classes": student.get_classes()}
    with open(path,'r+') as f:
        f.seek(0)
        content = f.read()
        content = json.loads(content)
        # add new student to json 
        content.append(student_dict)
        f.seek(0)        
        json.dump(content,f, indent=2)
        f.truncate()

def save_to_db(updated_db, path='./data/users.json'):
    with open(path,'w') as f:
        f.write(json.dumps(updated_db, indent=2))
        f.close()

def find_user_in_db(username: str, path='./data/users.json'):
    users = load_db(path)
    if username in users:
        return users[username]
    return None