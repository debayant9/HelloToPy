import json
from difflib import get_close_matches

jsonfile = json.load(open("data.json",'r'))
def diction(words):
    w = words.lower()
    if w in jsonfile:
        return jsonfile[w]
    elif words.title() in jsonfile:
       return jsonfile[words.title()]
    elif words.upper() in jsonfile:
       return jsonfile[words.upper()]
    elif len(get_close_matches(w, jsonfile.keys(), 3, 0.8)) > 0:
        potList = get_close_matches(w, jsonfile.keys(), 3, 0.8)
        intp = input("Did you meant %s? Enter Y/N :" % potList[0])

        if intp == "Y":
            return jsonfile[potList[0]]
        else:
            print("Please try again! Word does'nt exist")
            return 1
    else:
        print("Please try again! Word does'nt exist")
        return 1
#    try:
#        print(jsonfile[w])
#    except:
#        print("Word does not exist")


val = input("Please type your word : ")
out = diction(val)
if type(out) == list:
    for i in range(0, len(out)):
        print(out[i])
