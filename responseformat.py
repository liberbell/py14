import requests
from pprint import pprint
import json

resp_obj = requests.get("https://swapi.co/api/vehicles/4/")
print(resp_obj.status_code)
# pprint(resp_obj.json())
print(resp_obj.headers['content-type'])