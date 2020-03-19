import requests
from pprint import pprint
import json
import webbrowser

url = "https://www.wikipedia.org"
resp_obj = requests.get(url)

print(resp_obj.url)
print(resp_obj.status_code)

# print(webbrowser.open(resp_obj.url))

search_term = input("Enter the term you need to search: ")

URL = "https://www.youtube.com/search"
PARAMS = {'q': search_term}

r_get = requests.get(url = URL, params=PARAMS)
print(r_get.status_code)
print(r_get.url)
print(webbrowser.open(r_get.url))