import requests
from pprint import pprint

response = requests.get("https://gmail.com")
# print(response.history)
# print(response.url)

if response.history:
    print("Redirect history:")
    for resp in response.history:
        print(resp.status_code, resp.url)
    print("\nFinal destination:")
    print(response.status_code, response.url)

else:
    print("Request was not redirect.")