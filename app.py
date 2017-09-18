import json
from difflib import get_close_matches

data = json.load(open("data.json")) #Loads json file to a Python Dictionary

def fetch(word):

    if define in data.keys():

        return (data[word])

    else:

        if len(get_close_matches(word, data.keys())) == 0:

            return "This is embarrassing!! Word not found. Better luck next time"

        else:

            choice = input('Sorry, word not found. Did you mean %s instread? y/n ' % get_close_matches(word, data.keys())[0])

            if choice.lower() == 'y':

                return data[get_close_matches(word, data.keys())[0]]

            else:

                return "Bummer!! Seems like the word does not exist"

running = 1

while running == 1:
    define = input(">").lower()

    if define == 0:

        running = 0

    else:

        print(fetch(define))
