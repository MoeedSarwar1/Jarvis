ages = {"ali": 20, "sara": 25}
ages["omar"] = 30
ages["ali"] = 21
print(ages["ali"])
print(len(ages))
print(ages)


stock = {"pen": 3, "book": 0}
print(stock.get("book", 10))
print(stock.get("bag", 10))
print(stock.get("bag"))
print("done")


def word_count(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


print(word_count(["tea", "milk", "tea"]))  # {'tea': 2, 'milk': 1}
print(word_count([]))  # {}
print(word_count(["a"]))  # {"a":1}
