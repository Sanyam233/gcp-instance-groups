from flask import Flask, request
import json
import os
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", os.urandom(24))

CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/", methods=["GET"])
def main():
    name = os.getenv("NAME", "NAME-DEV")
    zone = os.getenv("ZONE", "ZONE-DEV")
    return json.dumps(dict(status="success", message=f"This container is {name} in zone {zone}"))

@app.route("/home", methods=["GET"])
def home():
    return json.dumps(dict(status="success", message="Working from home"))

@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print(f"client has connected {request.sid}", flush=True)
    emit("success",{"data":f"id: {request.sid} is connected"}, to=request.sid)

@socketio.on("vm_info")
def handle_vm_info():
    name = os.getenv("NAME", "NAME-DEV")
    zone = os.getenv("ZONE", "ZONE-DEV")
    print("GETTING VM INFO", name, zone, flush=True)
    emit("vm_info", {"data" : {"name" : name, "zone" : zone}})

@socketio.on("disconnect")
def disconnected(data):
    """event listener when client disconnects to the server"""
    print(f"user disconnected {request.sid}", flush=True)

@socketio.on_error()
def handle_socket_error(err):
    print("HEREEE", err, flush=True)

if __name__ == '__main__':
    if os.getenv("DEV_ENV") == "test":
        socketio.run(app)
    else:
        socketio.run(app, debug=True, host='0.0.0.0', port=8080)

