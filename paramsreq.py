import requests
from pprint import pprint
import json
import webbrowser

url = "https://www.wikipedia.org"
resp_obj = requests.get(url)
