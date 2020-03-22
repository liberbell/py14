import requests
from pprint import pprint

url = "https://swapi.co/api/people/3"
headers = {'user-agent': 'Google Chrome'}
resp = requests.get(url, headers=headers)
print(resp.status_code)