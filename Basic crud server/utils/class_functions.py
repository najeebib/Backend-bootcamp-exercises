import modules.school_class as SchoolClass
import modules.student as Student
from .db_functions import save_to_db

def check_class_in_db(class_db: dict, class_name: str):
    if type(class_name) != str or type(class_db) != dict:
        raise TypeError
    return class_name in class_db

def find_class_by_id(class_db: dict, class_id: int):
    if type(class_id) != int or type(class_db) != dict:
        raise TypeError
    # go through the students and look for student with id
    for _, class_into in class_db.items():
        if class_into["id"] == class_id:
            return class_into
    return None


def add_class(school_class: SchoolClass, classes_db: dict):
    if not isinstance(school_class, type(school_class)) or type(classes_db) != dict:
        raise TypeError
    if not check_class_in_db(classes_db, school_class.get_name()):
        # make a json object of the student
        class_dict = {"name":school_class.get_name(), "id": school_class.get_id(), "teacher":  school_class.get_teacher(), "topics": school_class.get_topics()}
        classes_db[school_class.get_id()] = class_dict
        save_to_db(classes_db, './data/classes.json')

def add_student_to_class(class_: SchoolClass, classes_db: dict,student: Student, students_db: dict):
    if str(class_.get_id()) in classes_db and student.get_name() in students_db:
        student_classes = students_db[student.get_name()]["classes"]
        student_classes.append(class_.get_name())
        students_db[student.get_name()]["classes"] = student_classes
        save_to_db(students_db, './data/students.json')