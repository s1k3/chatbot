import csv

import nltk
from nltk.tokenize import word_tokenize

stop_words = [
    "a", "an", "the", "is", "was", "been", "of", "for", "at"
]
devices = [
    "fan", "light"
]


def get_classifier():
    data=get_data()
    trainings=data['trainings']
    words=data['words']
    t = []
    for training in trainings:
        tokens = word_tokenize(training[0])
        attribute_set = {}
        for token in tokens:
            if token not in stop_words and token not in devices:
                attribute_set[token] = token in words
        t += [(attribute_set, training[1])]

    classifier = nltk.NaiveBayesClassifier.train(t)
    return classifier


def get_data():
    trainings = []
    # Read the training data set
    with open('training.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            comment = row['command'].lower()
            output = row['value']
            trainings += [(comment, output)]

    words = []
    for training in trainings:
        # Retrieve the actual command
        tokens = word_tokenize(training[0])
        for token in tokens:
            # remove the stop words
            if token not in stop_words and token not in devices:
                words += [token]
    words = set(words)
    return {
        'trainings': trainings,
        'words': words
    }
