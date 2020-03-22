import requests
from pprint import pprint
import webbrowser

url = "https://swapi.co/api/people/3"
headers = {'user-agent': 'Google Chrome'}
resp = requests.get(url, headers=headers)
print(resp.status_code)
print(resp.headers)
print(resp.headers['content-type'])

resp_obj = requests.get("https://en.wikipedia.org/wiki/Monty_Python")
print(resp_obj.headers)
# print(webbrowser.open(resp_obj.url))
print(resp_obj.request.headers)

r = requests.get("https://httpbin.org/user-agent", headers = {'User-Agent': 'Internet Explorer/2.0'})