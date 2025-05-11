from flask import Flask
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    name = os.getenv("NAME", "NAME-DEV")
    zone = os.getenv("ZONE", "ZONE-DEV")
    return json.dumps(dict(status="success", message=f"This container is {name} in zone {zone}"))

@app.route("/home", methods=["GET"])
def home():
    return json.dumps(dict(status="success", message="Working from home"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
