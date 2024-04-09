import utils.class_functions as fns
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
