import json
from difflib import get_close_matches

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        # yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        print("Word not found. Did you mean \'%s\' instead?" % get_close_matches(w, data.keys())[0])
        return data[get_close_matches(w, data.keys())[0]]
        # if yn == "Y":
        #     return data[get_close_matches(w, data.keys())[0]]
        # elif yn == "N":
        #     return "The word doesn't exist. Please double check it."
        # else:
        #     return "We didn't understand your entry."
    else:
        return "The word or similar words don't exist. Please double check it."

if __name__ == "__main__":
    data = json.load(open("data.json"))
    
    word = input("Enter word: ")
    output = meaning(word)
    i = 1
    if type(output) == list:
        for item in output:
            print(i, ". ", item, sep="")
            i += 1
    else:
        print(output)
