import requests
from pprint import pprint
import webbrowser

r_post = requests.post("https://en.wikipedia.org/w/index.php", data={'search' : 'george harrison'})
print(r_post.status_code)
print(type(r_post))
# pprint(r_post.text)
# print(webbrowser.open(r_post.url))

# with open('george.html', 'wb') as f:
#     for chunk in r_post.iter_content(chunk_size=10000):
#         f.write(chunk)

url = "https://httpbin.org/post"
files = {'files': open("test.txt", "rb")}
values = {"upload_files": "test.txt", "OUT" : "csv" }
print(files)

r_post = requests.post(url, files=files, data=values)
print(r_post.url)
pprint(r_post.text)