import requests
class ProfanityFilter:
    def __init__(self):
        # profanity filter api https://www.purgomalum.com/
        self.api_url = "https://www.purgomalum.com/service/json?text="
    # censor the message using the api
    def censor(self, message: str):
        request = self.api_url + message
        response = requests.get(request)
        return response.json()["result"]
