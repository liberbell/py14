import requests
from pprint import pprint
import json
import webbrowser

url = "https://www.wikipedia.org"
resp_obj = requests.get(url)

print(resp_obj.url)
print(resp_obj.status_code)

print(webbrowser.open(resp_obj.url))