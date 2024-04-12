import requests

ENDPOINT = "http://localhost:8000/auth"
user_body = {"username": "name","password": "123456", "is_admin": False}
def test_sign_up():
    # test if post request request is successful
    response = requests.post(ENDPOINT + "/sign_up", json=user_body)
    assert response.status_code == 200
    
    # test if post request request failed
    response = requests.post(ENDPOINT + "/sign_up")
    assert response.status_code == 422

def test_sign_in():
    # test if post request request is successful
    response = requests.post(ENDPOINT + "/sign_in", json=user_body)
    assert response.status_code == 200
    
    # test if post request request failed
    response = requests.post(ENDPOINT + "/sign_in")
    assert response.status_code == 422
    # test if request fails when sending wrong password
    wrong = {"username": "name","password": "1111111", "is_admin": False}
    response = requests.post(ENDPOINT + "/sign_in", json=wrong)
    assert response.status_code == 403

        # test if request fails when sending a user that doesnt exist
    wrong = {"username": "name 2 ","password": "123456", "is_admin": False}
    response = requests.post(ENDPOINT + "/sign_in", json=wrong)
    assert response.status_code == 404

