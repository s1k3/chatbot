import nltk
from nltk.tokenize import word_tokenize
import jaro_winkler
import output


def is_question(sentence):
    tokens = word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    devices = output.read_devices()
    if tags[0][1] == "VBZ" or tags[0][1] == "WP":
        details = jaro_winkler.devices(sentence)
        message = ''
        for key in details['device_list']:
            if details['device_list'][key] != '':
                message = message + " " + details['device_list'][key] + " is "

                if devices[key] == "1":
                    if tags[0][1] == "WP":
                        message = message + "powered on"
                    else:
                        message = "Yes it is."
                else:
                    if tags[0][1] == "WP":
                        message = message + "powered off"
                    else:
                        message = "No it is not."
        return message
    return ''


print(is_question("what is the status of bright"))
