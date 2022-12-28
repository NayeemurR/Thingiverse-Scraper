import requests
import json

url = "https://api.thingiverse.com/search/"
querystring = {"sort": "popular"}
headers = {
    "Authorization": "Bearer *****"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
response = json.loads(response.text)
# print(response)
data = response['hits']

# Get every item name and its public url
def get_urls():
    data_list = []
    for d in data:
        temp = (d["name"], d["public_url"])
        data_list.append(temp)
    return data_list


# item_ids = {}

# for i in data:
#     item_ids[i['name']] = i['id']
    
# # print(item_ids)

# for name in item_ids:
#     print(type(item_ids[name]))
#     url = f"https://api.thingiverse.com/things/files/{item_ids[name]}"
#     querystring = {}
#     headers = {
#         "Authorization": "Bearer ******"
#     }
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     response = json.loads(response.text)
#     print(response)

# /files/{$id}/
# url = "https://api.thingiverse.com/files/763622"

