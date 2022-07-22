from flask import Flask
from flask_restful import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import platform
import subprocess

app = Flask(__name__)
auth = HTTPBasicAuth()

#Словарь с данными аутентификации
users = {
    "john": generate_password_hash("hello")
}

#Верификация пользователей из словаря выше
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

#Обработка пост-запроса
@app.route('/api/get-result', methods=['POST'])
@auth.login_required
def post_query_json():
    data = request.get_json()
    response = {}
    for ip in data["ip"]:
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', parameter, '1', ip]
        result = subprocess.call(command) == 0
        response[ip] = result
    return response

#Обработка гет-запроса
@app.route('/api/<ip>', methods=['GET'])
def get_query_result(ip):
    result = {}
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '1', ip]
    response = subprocess.call(command) == 0
    result[ip] = response
    return result

#Запуск
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=30)
