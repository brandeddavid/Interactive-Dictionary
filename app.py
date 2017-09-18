import json
from difflib import get_close_matches

data = json.load(open("data.json")) #Loads json file to a Python Dictionary

def fetch(word):

    if define in data.keys():

        return (data[word])

    else:

        if len(get_close_matches(word, data.keys())) == 0:

            return "Word not found. Better luck next time"

        else:

            choice = input('Sorry, word not found. Did you mean ' + get_close_matches(word, data.keys())[0] + '? ')

            if choice == 'y':

                return data[get_close_matches(word, data.keys())[0]]

while True:

    define = input(">").lower()

    print(fetch(define))
