from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_hostname():
    hostname = socket.gethostname()
    return jsonify(hostname=hostname)

@app.route('/', methods=['POST'])
def start_process():
    subprocess.Popen(['python', 'stress_cpu.py'])

    return jsonify({"message": "started stress_cpu.py"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)