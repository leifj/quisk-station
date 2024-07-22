import requests

class StationAPI:
    def __init__(self,url):
        self.url = url

    def get(path):
        r = requests.get(self.url + path)
        return r.json()
