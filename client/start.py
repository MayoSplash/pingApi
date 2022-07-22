import requests
import json

#Читаем данные из файла
try:
    input = open("input.txt", mode="r")
except IOError as e:
    print("Не удалось открыть файл input.txt")
    input()
else:
    lines = []
    for line in input:
        lines.append(line)
    input.close()
    lines = [line.rstrip() for line in lines]

#Данные для отправки запроса
username = 'john'
password = 'hello'
url = "http://127.0.0.1:30/api/get-result"
headers = {"Content-type": "application/json"}
data = json.dumps({
    "ip": lines
})

#Получаем ответ
req = (requests.post(url=url, headers=headers, data=data, auth=(username, password)))

#Запись в JSON
with open("output.json", "w+") as output:
    output.writelines(str(req.text))
output.close()

#Запись в ТХТ
output = open("output.txt", "w+")
data = json.loads(req.text)
for key in data:
    output.write(key + "\t" + str(data[key]) + "\r")
output.close()

#Запись в CSV
output = open("output.csv", "w+")
data = json.loads(req.text)
for key in data:
    output.write(key + ";" + str(data[key]) + "\r")
output.close()





