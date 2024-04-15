import requests

ENDPOINT = "http://localhost:8000"
user_body = {"email": "name","password": "123456"}

def test_sign_in():
    # test if post request request is successful
    response = requests.post(ENDPOINT + "/sign_in", json=user_body)
    assert response.status_code == 200
    
    # test if post request request failed
    response = requests.post(ENDPOINT + "/sign_in")
    assert response.status_code == 422
    # test if request fails when sending wrong password
    wrong = {"email": "name","password": "1111111"}
    response = requests.post(ENDPOINT + "/sign_in", json=wrong)
    assert response.status_code == 403

