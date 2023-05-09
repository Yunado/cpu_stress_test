from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)


@app.route("/", methods=["POST"])
def stress_cpu():
    # Run stress_cpu.py in a separate process
    subprocess.Popen(["python3", "stress_cpu.py"], stdout=subprocess.PIPE)
    return "Started stressing CPU\n"


@app.route("/", methods=["GET"])
def get_ip():
    # Return private IP address of EC2 instance
    return socket.gethostname()


if __name__ == "__main__":
    app.run()
