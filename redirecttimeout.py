import requests
from pprint import pprint

response = requests.get("https://gmail.com")
print(response.history)