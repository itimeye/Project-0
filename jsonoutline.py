import json

dictionary = {
    "name" : "English 101",
    "schdule" : "Monday, Tuesday",
    "hour" : 12,
    "minute" : 45
    }

with open ('Classes.txt', 'w') as outfile:
    json.dump(dictionary, outfile)
