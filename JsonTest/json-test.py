import json

FILENAME = "file"

json.dump({'key': 5}, open(FILENAME + ".json", "w"))

users = json.load(open(FILENAME + ".json"))
print("JSON key: ", users['key'])
