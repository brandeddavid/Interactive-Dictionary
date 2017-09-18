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

            elif choice.lower() == 'n':

                return "Bummer!! I can't seem to get the word. Please double check it"

            else:

                return 'Am bright. But not that bright'

running = 1

while running == 1:
    define = input(">").lower()

    if define == 0:

        running = 0

    else:

        if type((fetch(define))) == list:

            for item in fetch(define):

                print(item)

        else:

            print(fetch(define))
