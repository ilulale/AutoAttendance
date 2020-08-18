import json

def cinfo(atr):
    f = open('cred.json')

    data = json.load(f)

    return data[atr]


