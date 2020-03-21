import requests
from pprint import pprint
import json

url = "htt@s://example.com"
r_head = requests.head("https://example.com")

print(r_head.status_code)