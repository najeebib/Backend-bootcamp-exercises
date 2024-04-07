import json
from modules.student import Student
from models.student_model import student_model


# read the data from the json file
def load_db(path):
    try:
        with open(path, "r") as f:
            content = f.read()
            content = json.loads(content)
            return content
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return
# add a new student to json file
def add_student(student: Student, path='./data/students.json'):
    # make a json object of the student
    student_dict = {"name":student.get_name(), "id": student.get_id(), "age":  student.get_age(), "classes": student.get_classes()}
    students = load_db(path)
    # add student to db
    students[student.get_name()] = student_dict
    print(students)
    save_to_db(students, './data/students.json')

def save_to_db(updated_db, path):
    try:
        with open(path,'w') as f:
            f.write(json.dumps(updated_db, indent=2))
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return

def find_user_in_db(username: str, path='./data/users.json'):
    users = load_db(path)
    if username in users:
        return users[username]
    return None

def find_student_by_id(id: int, path='./data/students.json'):
    students = load_db(path)
    # go through the students and look for student with id
    for _, student_info in students.items():
        if student_info["id"] == id:
            return student_info
    return None

def update_student(id: int,student: student_model, path='./data/students.json'):
    # find the user in the db
    student_old_info = find_student_by_id(id)
    if student_old_info:
        # get the user name
        old_name = student_old_info["name"]
        students = load_db(path)
        # make a new updated user with new data
        updated_student = {"name":student.name, "id": id, "age":  student.age, "classes": student.classes}
        # put the new data in the db
        students[old_name] = updated_student
        # if the name was updated, then update the key
        if student.name != old_name:
            students[student.name] = students.pop(old_name)
        save_to_db(students, path)

def delete_from_db(name: str, path='./data/students.json'):
    students = load_db(path)
    # find the user in the db
    if name in students:
        # delete the user and update db
        del students[name]
        save_to_db(students, path)


def delete_all_students(path='./data/students.json'):
    students = load_db(path)
    for student_name, _ in students.items():
        delete_from_db(student_name)
