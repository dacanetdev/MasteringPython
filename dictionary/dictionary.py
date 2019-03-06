import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def retrieve_definition(word):

  close_matches = get_close_matches(word, data.keys(), n=1, cutoff=0.5)
  word = word.lower()
  if word in data:
    return data[word]
  elif word.title() in data:
    return data[word.title()]
  elif len(close_matches) > 0:
     value = SequenceMatcher(None, word, close_matches[0]).ratio()
     print(value)
     result = input(f"Did you mean {close_matches[0]} it matches by {value*100}% [y or n]? ")
     if result == "y":
       return data[close_matches[0]]
     elif result == "n":
       return ("The word doesn't exist yet")
     else:
       return ("We don't understand the entry, apologies")
  else:
    return ("The word doesn't exist, please double check it.")

word_user = input('Enter a word: ')

output = retrieve_definition(word_user)

if type(output) == list:
  for item in output:
    print("-", item)
else:
  print("-", output)