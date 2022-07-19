from flask import Flask
from flask_restful import request
import platform
import subprocess
import json

app = Flask(__name__)

@app.route('/api/json', methods=['POST'])
def json():
    data = request.get_json()

    result = {}
    for ip in data["ip"]:
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', parameter, '1', ip]
        response = subprocess.call(command) == 0
        result[ip] = response

    return result

@app.route('/api/check/<ip>', methods=['GET'])
def check(ip):
    result = {}
    parameter = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parameter, '1', ip]
    response = subprocess.call(command) == 0
    result[ip] = response
    return result


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=30)
