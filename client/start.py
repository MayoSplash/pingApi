import csv

import requests
import json

input = open("input.txt", mode="r")
lines = []
for line in input:
    lines.append(line)
input.close()
lines = [line.rstrip() for line in lines]

username = 'john'
password = 'hello'
url = "http://127.0.0.1:30/api/get-json"
headers = {"Content-type": "application/json"}
data = json.dumps({
    "ip": lines
})

req = (requests.post(url=url, headers=headers, data=data, auth=(username, password)))
with open("output.txt", "w+") as output:
    output.writelines(str(req.text))
    output.close()


output = open("output.csv", "w+")
data = json.loads(req.text)
for key in data:
    output.write(key + ";" + str(data[key]) + "\r")

output.close()





