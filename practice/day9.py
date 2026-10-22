name = "  Ali  "
name.strip()
print(len(name))
name = name.strip()
print(len(name))
print("tea milk tea".split(" "))
print("Ali".lower() == "ali")

item = "tea"
qty = 3
price = 50
print(f"{qty} x {item} = {qty * price}")
print(f"{item.upper()}!")
print("{item} costs {price}")


def is_blank(string):
    name = string.strip()
    if name == "":
        return True
    else:
        return False


print(is_blank("      hi       "))  # exceped False
print(is_blank("hi"))  # expected Fasle
print(is_blank(""))  # expected true


def initials(full_name):
    full_initials = ""
    initial = full_name.split(" ")
    for w in initial:
        name = w[0]
        full_initials = full_initials + name[0].upper()

    return full_initials


print(initials("moeed sarwar"))  # expected MS
print(initials("moeed sarwar khokhar"))  # expected MS
