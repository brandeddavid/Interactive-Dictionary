import json

data = json.load(open("data.json")) #Loads json file to a Python Dictionary

def fetch(word):

    if define in data.keys():

        return (data[word])

    else:

        return "Word not found. Better luck next time"

define = input(">").lower()

print(fetch(define))
