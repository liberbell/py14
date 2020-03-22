import requests
from pprint import pprint
import json

r_put = requests.put("https://httpbin.org/put", data = {'key' : 'value'})
print(r_put.status_code)
# print(r_put.text)

r_options = requests.options("https://httpbin.org/get")
print(r_options.status_code)
print(type(r_options))
pprint(r_options.headers)