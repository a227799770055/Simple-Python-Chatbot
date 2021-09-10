import requests
import json

data = {'key':'I want to search for blood pressure'}

def request():
    url = 'http://localhost:3000/botrespon'
    get = requests.post(url, data=data)
    print(get.text)
if __name__ == '__main__':
    request()