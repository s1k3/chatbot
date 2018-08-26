from flask import Flask
from flask import jsonify
import nltk
import naive_bayes
from nltk.tokenize import word_tokenize

app = Flask(__name__)


@app.route("/comment")
def comment():
    sentence = 'This is a sentence.'
    tokens = nltk.word_tokenize(sentence)
    return tokens[2]


@app.route("/")
def index():
    classifier = naive_bayes.get_classifier()

    test_sentence = "turn on the light"
    test_sent_features = {}
    tokens = word_tokenize(test_sentence.lower())
    words = naive_bayes.get_data()['words']
    for token in tokens:
        test_sent_features[token] = token in words

    response = {
        'yes': "{0:.2f}".format(classifier.prob_classify(test_sent_features).prob("yes") * 100),
        'no': "{0:.2f}".format(classifier.prob_classify(test_sent_features).prob("no") * 100)
    }

    return jsonify(response)


@app.route("/devices")
def devices():
    return "Status of the devices"


if __name__ == "__main__":
    app.run(debug=True)
