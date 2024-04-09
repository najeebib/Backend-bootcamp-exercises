from modules.student import Student
from models.student_model import student_model
from .db_functions import save_to_db
def check_student_in_db(student_db: dict, student_name):
    if type(student_name) != str or type(student_db) != dict:
        raise TypeError
    return student_name in student_db

def add_student(student: Student, student_db: dict):
    if not isinstance(student, type(student)) or type(student_db) != dict:
        raise TypeError
    if not check_student_in_db(student_db, student.get_name()):
        # make a json object of the student
        student_dict = {"name":student.get_name(), "id": student.get_id(), "age":  student.get_age(), "classes": student.get_classes()}
        student_db[student.get_name()] = student_dict
        save_to_db(student_db, './data/students.json')

def find_student_by_id(id: int, student_db: dict):
    if type(id) != int or type(student_db) != dict:
        raise TypeError
    # go through the students and look for student with id
    for _, student_info in student_db.items():
        if student_info["id"] == id:
            return student_info
    return None

def update_student(id: int,student: student_model, student_db: dict):
    # find the user in the db
    student_old_info = find_student_by_id(id, student_db)
    if student_old_info:
        # get the user name
        old_name = student_old_info["name"]
        # make a new updated user with new data
        updated_student = {"name":student.name, "id": id, "age":  student.age, "classes": student.classes}
        # put the new data in the db
        student_db[old_name] = updated_student
        # if the name was updated, then update the key
        if student.name != old_name:
            student_db[student.name] = student_db.pop(old_name)
        save_to_db(student_db, './data/students.json')

def delete_student(name: str, student_db: dict):
    # find the user in the db
    if name in student_db:
        # delete the user and update db
        del student_db[name]
        save_to_db(student_db, './data/students.json')

def delete_all_students(student_db: dict):
    # make a copy of all student to delete to avoid runtime error
    students_to_delete = list(student_db.keys())
    
    for student_name in students_to_delete:
        del student_db[student_name]
    
    save_to_db(student_db, './data/students.json')

