import utils.auth_functions as fns
import pytest
def test_check_class_type():
    assert type(fns.check_user_in_db("name", {})) == bool

def test_check_class_in_db():
    assert fns.check_user_in_db("name", {}) == False

    assert fns.check_user_in_db( "name", {"name":{"username": "name","password": "$2b$12$EcJ3pckV7BLyHEQnyMbxWeULbm6OEXoxV.QpUYUeRopmSqX9BuSi2", "is_admin": True}}) == True

    assert fns.find_user_in_db("name", {"name": {}}) == {}
    assert fns.find_user_in_db("name", {}) == None
def test_check_input():
    with pytest.raises(TypeError):
        fns.check_user_in_db({"math":{"id": 1,"name": "math", "teacher": "Salem", "topics": ["agebra"]}}, 1)
        fns.check_user_in_db("math","math")
        fns.check_user_in_db("math",1)

        fns.find_user_in_db({"math":{"id": 1,"name": "math", "teacher": "Salem", "topics": ["agebra"]}}, 1)
        fns.find_user_in_db("math","math")
        fns.find_user_in_db("math",1)
