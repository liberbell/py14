import requests
from pprint import pprint

resp_obj = requests.get("https://httpbin.org/")
print(resp_obj.status_code)
print(resp_obj.encoding)

resp_obj.encoding = "ISO 8859-1"
print(resp_obj.encoding)

resp_obj = requests.get("https://github.com/timeline.json")
print(resp_obj.status_code)
print(resp_obj.encoding)
pprint(resp_obj.text)
resp_obj.encoding = "ISO 8859-1"
print(resp_obj.encoding)
pprint(resp_obj.text)