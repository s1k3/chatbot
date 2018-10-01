from nltk.tokenize import word_tokenize
from similarity.jarowinkler import JaroWinkler


def devices(sentecte, theshold=80):
    jarowinkler = JaroWinkler()
    device_list = {"fan": "", "light": ""}
    names = []
    light_words = ["light", "lamb", "bulb", "torch"]
    fan_words = ["fan", "blade", "ventilator", "vane"]
    tokens = word_tokenize(sentecte)
    for token in tokens:
        flag = 0
        for word in light_words:
            percentage = jarowinkler.similarity(token, word) * 100
            if percentage >= 80:
                device_list["light"] = token
                flag = 1
                names += [token]
                break
        if flag == 1:
            break
    for token in tokens:
        flag = 0
        for word in fan_words:
            percentage = jarowinkler.similarity(token, word) * 100
            if percentage >= 80:
                device_list["fan"] = token
                flag = 1
                names += [token]
                break
        if flag == 1:
            break

    return {
        "device_list": device_list,
        "names": names
    }
