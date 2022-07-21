from flask import Flask
from flask_restful import request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import platform
import subprocess

users = {
    "john": generate_password_hash("hello")
}

app = Flask(__name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route('/api/json', methods=['POST'])
@auth.login_required
def post_query_result():
    data = request.get_json()
    result = {}
    for ip in data["ip"]:
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', parameter, '1', ip]
        response = subprocess.call(command) == 0
        result[ip] = response
    return result

@app.route('/api/check/<ip>', methods=['GET'])
def get_query_result(ip):
    result = {}
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '1', ip]
    response = subprocess.call(command) == 0
    result[ip] = response
    return result

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=30)
