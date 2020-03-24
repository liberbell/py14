import requests
from pprint import pprint

ok_resp = requests.get("https://example.com")
print(ok_resp.status_code)