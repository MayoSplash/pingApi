from flask import Flask
from flask_restful import Api, Resource, request
import platform
import subprocess

app = Flask(__name__)
api = Api(prefix="/api")

class Ping(Resource):
    def get(self, ip):
        parameter = '-n' if platform.system().lower() == 'windows' else '-c'

        command = ['ping', parameter, '1', ip]
        response = subprocess.call(command)
        response = response == 0

        result = {ip: response}
        return result

api.add_resource(Ping, "/<ip>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=30)
