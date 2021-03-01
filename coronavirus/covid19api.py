import json
import requests

class Coronavirusapi:
    username = ""
    password = ""
    token = ""
    endpoint = "https://api.covid19api.dev/"

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def getToken(self):
        response = ""
        url = self.endpoint + "token"
        payload = {"username": self.username, "password": self.password}
        headers = {
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
            response = json.loads(response.text)
            self.token = response['Document']
        except Exception as e:
            print(response)


    def getMonth2020(self, endpoint):
        self.getToken()
        url = self.endpoint + endpoint
        payload = {}
        headers = {
            "Authorization": "Bearer " + self.token,
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request("GET", url, headers=headers, data=json.dumps(payload))

            return json.loads(response.text)
        except Exception as e:
            print(e)


    def getTimeSeries(self, endpoint):
        self.getToken()
        url = self.endpoint + endpoint
        payload = {}
        headers = {
            "Authorization": "Bearer " + self.token,
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", url, headers=headers, data=json.dumps(payload))

        return json.loads(response.text)




