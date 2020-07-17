import requests
import json

class ApiVideoHelper:
    def __init__(self):
        self.headers = {'content-type': 'application/json'}

    def login(self,api_key):
        payload = {"apiKey": api_key}
        response = requests.request("POST", "https://ws.api.video/auth/api-key", data=json.dumps(payload),
                                    headers=self.headers)
        json_response = response.json()
        self.headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + json_response['access_token']}
        return json_response

    def createVideoContainer(self,videoName):
        payload = {"title": videoName,"description":"deep fake video","mp4Support":True}
        response = requests.request("POST", "https://ws.api.video/videos", data=json.dumps(payload), headers=self.headers)
        json_response = response.json()
        return json_response

    def upload(self, videoBytes,videoName):
        response = self.createVideoContainer(videoName)
        uri = response['source']['uri']

        file = {'file': videoBytes}
        if 'content-type' in self.headers:
            del self.headers['content-type']
        response = requests.request("POST", "https://ws.api.video" + uri ,files=file, headers=self.headers)
        return 'Uploaded correctly'