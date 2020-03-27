import requests
from pprint import pprint
from requests import exceptions

# print(requests.get("https://nonexistent.com"))

# try: requests.get("https://nonexistent.com")
# except exceptions.ConnectionError:
#     print("Error: Connection Error")

requests.get("https://github.com/", timeout=0.01)