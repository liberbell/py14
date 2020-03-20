import requests
from pprint import pprint

r_post = requests.post("https://en.wikipedia.org/w/index.php", data={'search' : 'george harison'})
print(r_post.status_code)