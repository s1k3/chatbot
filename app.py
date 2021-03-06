from flask import Flask
from flask import jsonify
from flask import request
import nltk
import naive_bayes
from nltk.tokenize import word_tokenize
import jaro_winkler
import output
import wh_question

app = Flask(__name__)


@app.route("/comment")
def comment():
    sentence = 'This is a sentence.'
    tokens = nltk.word_tokenize(sentence)
    return tokens[2]


@app.route("/", methods=["GET", "POST"])
def index():
    sentence = ""
    classifier = naive_bayes.get_classifier()
    if request.method == 'POST':
        sentence = request.form['command']
    else:
        sentence = request.args.get('command')
    question = wh_question.is_question(sentence)
    if question != '':
        return question
    sentence_features = {}
    devices = jaro_winkler.devices(sentence)
    tokens = word_tokenize(sentence.lower())
    words = naive_bayes.get_data()['words']
    for token in tokens:
        sentence_features[token] = token in words

    response = {
        'yes': int(classifier.prob_classify(sentence_features).prob("yes") * 100),
        'no': int(classifier.prob_classify(sentence_features).prob("no") * 100)
    }
    # check the devices
    if len(devices['names']) == 1:
        if response['yes'] > response['no']:
            for key in devices['device_list']:
                if devices['device_list'][key] != '':
                    output.change_device(key, "1")
            return devices["names"][0] + " is turned on"
        elif response['yes'] < response['no']:
            for key in devices['device_list']:
                if devices['device_list'][key] != '':
                    output.change_device(key, "0")
            return devices["names"][0] + " is turned off"
        else:
            return "Sorry Could not understand that"
    elif len(devices['names']) == 0:
        return "your device name is wrong"

    return str(response['yes']) + ' ' + str(response['no'])


@app.route("/devices")
def devices():
    devices = output.read_devices()
    return jsonify(devices)


if __name__ == "__main__":
    app.run(debug=True)
