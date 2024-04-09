import utils.student_functions as fns
from modules.student import Student
from models.student_model import student_model
import pytest

def test_check_class_type():
    assert type(fns.check_student_in_db({}, "najeeb")) == bool

def test_check_class_in_db():
    assert fns.check_student_in_db({}, "math") == False

    assert fns.check_student_in_db({"najeeb":{"id": 1,"name": "najeeb", "age":25, "classes": []}}, "najeeb") == True

def test_input():
    with pytest.raises(TypeError):
        fns.check_student_in_db({"najeeb":{"id": 1,"name": "najeeb", "age":25, "classes": ["agebra"]}}, 1)
        fns.check_student_in_db("math","math")
        fns.check_student_in_db("math",1)
        fns.add_student("", [])
        fns.find_student_by_id({}, 1)

def test_add_delete_student():
    student = Student("najeeb", 1, 25, [])
    fns.add_student(student, {})
    db = {"najeeb":{"id": 1,"name": "najeeb", "age":25, "classes": []}}
    assert fns.check_student_in_db(db, "najeeb") == True
    assert fns.find_student_by_id(1, db) == {"id": 1,"name": "najeeb", "age":25, "classes": []}

    fns.delete_student("najeeb", db)
    assert fns.check_student_in_db(db, "najeeb") == False
