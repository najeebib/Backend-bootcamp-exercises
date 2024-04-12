import requests

ENDPOINT = "http://localhost:8000/class/classes"
admin_header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIHJvbGUiOiJhZG1pbiJ9.nP7CeitFDM6T_MXPrZg3oCtFadX31eAcMKD2F0m20CM"}
login_header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIHJvbGUiOiJndWVzdCJ9.ZFKt7tRDGZ0qeGXXedxwPFHcdimAyvBpOOn1mUwluIA"}
class_body = {"name": "name","id": 2, "teacher": "teacher", "topics": []}
def test_get_students():
    # test if get all classes request is successful
    response = requests.get(ENDPOINT, headers=login_header)
    assert response.status_code == 200
    # test if get all classes request failed when user isnt logged in
    response = requests.get(ENDPOINT)
    assert response.status_code == 401

def test_post_class():
    # test if post request request is successful
    response = requests.post(ENDPOINT, headers=admin_header, json=class_body)
    assert response.status_code == 200
    # test if post class request failed when user isnt an
    response = requests.post(ENDPOINT, headers=login_header, json=class_body)
    assert response.status_code == 401
    # test if post class failed when trying to make same class again
    response = requests.post(ENDPOINT, headers=admin_header, json=class_body)
    assert response.status_code == 403
    # test if post class failed when body isnt sent
    response = requests.post(ENDPOINT, headers=admin_header)
    assert response.status_code == 422

def test_post_student():
    student_body = {"name": "name","id": 5, "age": 25, "classes": []}
    # test if post request request is successful
    response = requests.post("http://localhost:8000/school/students", headers=admin_header, json=student_body)
    assert response.status_code == 200

    response = requests.post(ENDPOINT+"/2/5", headers=admin_header)
    assert response.status_code == 200

def test_get_students_in_class():
    response = requests.get(ENDPOINT+ "/name", headers=admin_header)
    assert response.status_code == 200
    assert len(response.json()) > 0