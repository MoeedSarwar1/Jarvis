import json

items = ["pen", "cup"]
with open("items.json", "w") as f:
    json.dump(items, f)
items.append("bag")
with open("items.json", "r") as f:
    loaded = json.load(f)
print(loaded)
print(items)


with open("pets.txt", "w") as f:
    f.write("cat\n")

with open("pets.txt", "w") as f:
    f.write("dog\n")

with open("pets.txt", "r") as f:
    print(f.read())
