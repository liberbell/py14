import requests
from pprint import pprint
import json

resp = requests.get("https://swapi.co/api/vehicles/4/")
print(resp.status_code)