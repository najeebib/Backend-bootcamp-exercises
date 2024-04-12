import requests

ENDPOINT = "http://localhost:8000/school/students"
admin_header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIHJvbGUiOiJhZG1pbiJ9.nP7CeitFDM6T_MXPrZg3oCtFadX31eAcMKD2F0m20CM"}
login_header = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIHJvbGUiOiJndWVzdCJ9.ZFKt7tRDGZ0qeGXXedxwPFHcdimAyvBpOOn1mUwluIA"}
student_body = {"name": "name","id": 1, "age": 25, "classes": []}
def test_get_students():
    # test if get all students request is successful
    response = requests.get(ENDPOINT, headers=login_header)
    assert response.status_code == 200
    # test if get all students request failed when user isnt logged in
    response = requests.get(ENDPOINT)
    assert response.status_code == 401
def test_post_student():
    # test if post request request is successful
    response = requests.post(ENDPOINT, headers=admin_header, json=student_body)
    assert response.status_code == 200
    # test if post student request failed when user isnt logged in
    response = requests.post(ENDPOINT, headers=login_header, json=student_body)
    assert response.status_code == 401
    # test if post request failed when trying to make same student again
    response = requests.post(ENDPOINT, headers=admin_header, json=student_body)
    assert response.status_code == 403
    # test if post request failed when body isnt sent
    response = requests.post(ENDPOINT, headers=admin_header)
    assert response.status_code == 422

def test_get_student():
    # test if get all students request is successful
    response = requests.get(ENDPOINT+"/1", headers=login_header)
    assert response.status_code == 200
    # test if get student failes when trying to get a student that doesnt exist
    response = requests.get(ENDPOINT+"/2", headers=login_header)
    assert response.status_code == 404

def test_put_student():
    
    response = requests.get(ENDPOINT + "/1", headers=login_header)
    assert response.status_code == 200
    assert response.json()["name"] == "name"
    # test if put requests is successful
    new_student = {"name": "name 2","id": 1, "age": 25, "classes": []}
    response = requests.put(ENDPOINT+"/1", headers=admin_header, json=new_student)
    assert response.status_code == 200
    # test if the name has changed
    response = requests.get(ENDPOINT + "/1", headers=login_header)
    assert response.status_code == 200
    assert response.json()["name"] == "name 2"

def test_delete_student():
    # test if the delete failes when trying to delete a user that doesnt exist
    response = requests.delete(ENDPOINT + "/2", headers=admin_header)
    assert response.status_code == 404
    # test if the delete failes when a user that isnt authorized tries to delete
    response = requests.delete(ENDPOINT + "/1", headers=login_header)
    assert response.status_code == 401
    # test if the delete request is successful
    response = requests.delete(ENDPOINT + "/1", headers=admin_header)
    assert response.status_code == 200
    # test if the db is empty
    response = requests.get(ENDPOINT, headers=login_header)
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_delete_all_students():
    response = requests.post(ENDPOINT, headers=admin_header, json=student_body)
    assert response.status_code == 200
    # test if the delete failes when a user that isnt authorized tries to d
    response = requests.delete(ENDPOINT, headers=login_header)
    assert response.status_code == 401
    # test if the delete request is successful
    response = requests.delete(ENDPOINT, headers=admin_header)
    assert response.status_code == 200
    # test if the db is empty
    response = requests.get(ENDPOINT, headers=login_header)
    assert response.status_code == 200
    assert len(response.json()) == 0





