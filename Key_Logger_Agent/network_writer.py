from writer import Writer
import requests


class NetworkWriter(Writer):
    def write(self,data):
        response = requests.post("http://127.0.0.1:5000/save_data", json= data)