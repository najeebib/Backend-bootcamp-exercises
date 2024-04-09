import utils.class_functions as fns
from modules.school_class import SchoolClass
import pytest
def test_check_class_type():
    assert type(fns.check_class_in_db({}, "math")) == bool

def test_check_class_in_db():
    assert fns.check_class_in_db({}, "math") == False

    assert fns.check_class_in_db({"math":{"id": 1,"name": "math", "teacher": "Salem", "topics": ["agebra"]}}, "math") == True

def test_check_input():
    with pytest.raises(TypeError):
        fns.check_class_in_db({"math":{"id": 1,"name": "math", "teacher": "Salem", "topics": ["agebra"]}}, 1)
        fns.check_class_in_db("math","math")
        fns.check_class_in_db("math",1)

def test_add_class_input():
    with pytest.raises(TypeError):
        fns.add_class("math", [])

def test_find_class_input():
    with pytest.raises(TypeError):
        fns.find_class_by_id([], "math")

def test_add_class():
    school_class = SchoolClass("math", 1, "saleem", ["agebra"])
    fns.add_class(school_class, {})
    assert fns.check_class_in_db({"math":{"id": 1,"name": "math", "teacher": "Salem", "topics": ["agebra"]}}, "math") == True 
    assert fns.find_class_by_id({"math":{"id": 1,"name": "math", "teacher": "Salem", "topics": ["agebra"]}}, 1) == {"id": 1,"name": "math", "teacher": "Salem", "topics": ["agebra"]}
    
def test_find_by_id():
    assert fns.find_class_by_id({}, 1) == None
