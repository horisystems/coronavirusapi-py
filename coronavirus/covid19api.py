import datetime
import json
import requests
import os.path, time


class Coronavirusapi:
    username = ""
    password = ""
    token = ""
    endpoint = "https://api.covid19api.dev/"

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.checkToken()

    def checkToken(self):
        token_file = "token.txt"

        current_date_and_time = os.path.getmtime(token_file)

        if (time.time() - current_date_and_time) / 3600 > 24 * 2:
            f = open(token_file, "w")
            self.getToken()
            f.write(self.token)
            f.close()
            time.sleep(3)
        else:

            f = open(token_file, "r")
            lines = f.readlines()
            self.token = lines[0]
            f.close()

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
        url = self.endpoint + endpoint
        headers = {
            "Authorization": "Bearer " + self.token,
            'Content-Type': 'application/json'
        }
        try:
            response = requests.request("GET", url, headers=headers)
            return json.loads(response.text)
        except Exception as e:
            print(e)

    def getTimeSeries(self, endpoint):
        url = self.endpoint + endpoint
        headers = {
            "Authorization": "Bearer " + self.token,
            'Content-Type': 'application/json',
        }
        response = requests.request("GET", url, headers=headers)
        return json.loads(response.text)
