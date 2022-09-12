import json
import requests

filename = 'data/hacker_news.json'

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
headers = {'Accept': 'application/json'}

r = requests.get(url, headers=headers)
resp_cnt = r.json()
with open(filename, 'w') as f:
    json.dump(resp_cnt, f, indent=4)
