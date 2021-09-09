import requests
import json

url = 'http://127.0.0.1:3000/'
get = requests.get(url)
print(get.status_code)
print('?????')
  