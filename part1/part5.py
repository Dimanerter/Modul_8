import json

data = {'name':"Гупало Василь", "age":30, "isStudent": True}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)