import requests
import json

url = "https://api.thingiverse.com/search/"
querystring = {"sort": "popular"}
headers = {
    "Authorization": "Bearer **********"
    }


response = requests.request("GET", url, headers=headers, params=querystring)
response = json.loads(response.text)
print(response)