import requests
from pprint import pprint
import json

r_put = requests.put("https://httpbin.org/put", data = {'key' : 'value'})
print(r_put.status_code)
print(r_put.text)