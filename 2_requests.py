import requests
from requests import status_codes

res = requests.get("http://google.com")
res.raise_for_status() # when error occured an error message is displaying

print("response : ", res.status_code) # 200 means working

# if res.status_code == requests.codes.ok:
#     print("works fine")
# else:
#     print("Error occured. [error code : ", res.status_code,"]")

