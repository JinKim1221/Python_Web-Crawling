import requests
from requests import status_codes
from requests.api import head
url = "http://google.com"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}

res = requests.get(url, headers=headers)
res.raise_for_status() # when error occured an error message is displaying

print("response : ", res.status_code) # 200 means working

with open("test.html", "w", encoding="utf8") as test:
    test.write(res.text)