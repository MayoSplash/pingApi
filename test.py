import requests
import json

url = "http://127.0.0.1:30/api/json"
headers = {"Content-type": "application/json"}
data = json.dumps({
    "ip": ["8.8.8.8", "127.0.0.1:30", "55.55.22.12"]
})


req = requests.post(url=url, headers=headers, data=data)

print(req.text)
