import requests
from pprint import pprint
import json

print(requests.__version__)
print(requests.__copyright__)

r_get = requests.get("https://www.metaweather.com/api/location/2487956/2020/03/17")
print(r_get.status_code)
# print(r_get.data)
print(type(r_get))
print(type(r_get.headers))
pprint(r_get.headers)

data = json.loads(r_get.text)
pprint(data)

print(r_get.is_redirect)