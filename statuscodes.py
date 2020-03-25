import requests
from pprint import pprint

ok_resp = requests.get("https://example.com")
print(ok_resp.status_code)
print(ok_resp.ok)

bad_resp = requests.get("https://www.yahoo.com/alf2adfd5")
print(bad_resp.status_code)
# print(bad_resp.ok)
# print(bad_resp.raise_for_status())
# print(ok_resp.raise_for_status())
print(type(ok_resp.headers))