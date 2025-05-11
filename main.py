from flask import Flask
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return json.dumps(dict(status="success", message="Working"))

@app.route("/home", methods=["GET"])
def home():
    return json.dumps(dict(status="success", message="Working from home"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
