import psutil
import socket
from flask import Flask, jsonify, render_template

app = Flask(__name__)


def get_details():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@app.route("/cpu")
def get_cpu_percentage():
    cpu_percent = psutil.cpu_percent()
    return jsonify({"cpu_percent": cpu_percent})

@app.route("/")
def hello_world():
    return "<p>Testing Argo</p>"

@app.route("/details")
def detail():
    hostname, ip = get_details()
    return render_template("index.html", HOSTNAME=hostname, IP=ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
