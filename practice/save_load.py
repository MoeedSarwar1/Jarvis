import json

items = ["tea", "milk"]

with open("shopping.json", "w") as f:
    json.dump(items, f)

with open("shopping.json", "r") as f:
    loaded = json.load(f)

print(loaded)
