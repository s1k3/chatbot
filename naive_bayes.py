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
    t = []
    for training in trainings:
        tokens = word_tokenize(training[0])
        attribute_set = {}
        for token in tokens:
            if token not in stop_words and token not in devices:
                attribute_set[token] = token in words
        t += [(attribute_set, training[1])]

    classifier = nltk.NaiveBayesClassifier.train(t)
    test_sentence = "run the fan"
    test_sent_features = {}
    tokens=word_tokenize(test_sentence.lower())
    for token in tokens:
        # if token  not in stop_words and token not in devices:
        test_sent_features[token]=token in words
    print(test_sent_features)
    print(test_sentence + "," + classifier.classify(test_sent_features))
    sum=(classifier.prob_classify(test_sent_features).prob("yes") * 100)+classifier.prob_classify(test_sent_features).prob("no") * 100
    print("Sum: ",sum)
    print("Yes:",(classifier.prob_classify(test_sent_features).prob("yes") * 100),
          "No:",classifier.prob_classify(test_sent_features).prob("no") * 100,
          "None",classifier.prob_classify(test_sent_features).prob(None))


get_classifier()

