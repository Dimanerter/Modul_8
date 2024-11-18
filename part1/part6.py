import json

with open("data.json", "r", encoding="utf-8") as f:
    data_from_json = json.load(f)
    print(data_from_json)