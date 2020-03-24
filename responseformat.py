import requests
from pprint import pprint
import json

resp_obj = requests.get("https://swapi.co/api/vehicles/4/")
print(resp_obj.status_code)
# pprint(resp_obj.json())
print(resp_obj.headers['content-type'])

resp = requests.get("https://www.yahoo.co.jp")
# pprint(resp.json())
print(resp.headers['content-type'])

resp_obj = requests.get("https://maps.googleapis.com/maps/api/geocode/json")
print(resp_obj.status_code)
pprint(resp_obj.json())

resp_obj = requests.get("https://swapi.co/api/vehicles/4", stream=True)
print(resp_obj.status_code)
# print(resp_obj.raw.read(10))

with requests.get("https://swapi.co/api/vehicles/4", stream=True) as response:
    with open("raw_file.txt", "wb") as b:
        for chunk in response.iter_content(1000):
            b.write(chunk)