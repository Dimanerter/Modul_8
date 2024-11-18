import json

data = {'name':"Gupalo Vasyl", "age":30, "isStudent": True}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)