import json
from difflib import get_close_matches

def explain(word):
    # Load dictionary
    dictionary = json.load(open('data.json'))

    if word in dictionary:
        return dictionary[word]
    elif word.capitalize() in dictionary: # for country names such as Paris
        return dictionary[word.capitalize()]
    elif word.upper() in dictionary: # for abbreviations such as USA
        return dictionary[word.upper()]
    # Guess closest word
    elif len(get_close_matches(word, dictionary.keys(), cutoff=0.8)) > 0:
        closest_match = get_close_matches(word, dictionary.keys(), cutoff=0.8)[0]
        # Get user input to confirm if we guessed the typo error
        while True:
            yes_no = input('Do you mean "{}"? Press y or n: '.format(closest_match))
            yes_no = yes_no.lower()
            if yes_no == 'y':
                return(dictionary[closest_match])
            elif yes_no == 'n':
                return 'Goodbye.'
    else:
        return 'Word not found.'

def main():
    # Get word from user
    word = input("Hi I'm a dictionary, enter a word to get its meaning: ")
    word = word.lower()

    results = explain(word)
    if type(results) == list:
        for result in results:
            print(result)
    else:
        print(results)

if __name__ == '__main__':
    main()