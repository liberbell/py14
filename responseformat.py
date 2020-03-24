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