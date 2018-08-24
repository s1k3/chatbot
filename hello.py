from flask import Flask

app = Flask(__name__)


@app.route("/comment")
def comment():
    return "Hello World!"


@app.route("/")
def index():
    return "Hello World!"


@app.route("/devices")
def devices():
    return "Status of the devices"


if __name__ == "__main__":
    app.run(debug=True, port=33507)
