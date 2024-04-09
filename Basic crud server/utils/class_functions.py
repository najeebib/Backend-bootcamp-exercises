import modules.class_ as Class
import modules.student as Student
from .db_functions import save_to_db

def check_class_in_db(class_db: dict, class_name: str):
    if type(class_name) != str or type(class_db) != dict:
        raise TypeError
    return class_name in class_db

def find_class_by_id(class_db: dict, class_id: int):
    # go through the students and look for student with id
    for _, class_into in class_db.items():
        if class_into["id"] == class_id:
            return class_into
    return None


def add_class(class_: Class, classes_db: dict):
    if not check_class_in_db(classes_db, class_.get_name()):
        # make a json object of the student
        class_dict = {"name":class_.get_name(), "id": class_.get_id(), "teacher":  class_.get_teacher(), "topics": class_.get_topics()}
        classes_db[class_.get_id()] = class_dict
        save_to_db(classes_db, './data/classes.json')

def add_student_to_class(class_: Class, classes_db: dict,student: Student, students_db: dict):
    if str(class_.get_id()) in classes_db and student.get_name() in students_db:
        student_classes = students_db[student.get_name()]["classes"]
        student_classes.append(class_.get_name())
        students_db[student.get_name()]["classes"] = student_classes
        save_to_db(students_db, './data/students.json')