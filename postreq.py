import requests
from pprint import pprint
import webbrowser

r_post = requests.post("https://en.wikipedia.org/w/index.php", data={'search' : 'george harrison'})
print(r_post.status_code)
print(type(r_post))
print(webbrowser.open(r_post.url))