from flask import Flask
import nltk
app = Flask(__name__)


@app.route("/comment")
def comment():
    sentence = 'This is a sentence.'
    tokens = nltk.word_tokenize(sentence)
    return tokens[2]


@app.route("/")
def index():
    return "Hello World!"


@app.route("/devices")
def devices():
    return "Status of the devices"


if __name__ == "__main__":
    app.run(debug=True)
