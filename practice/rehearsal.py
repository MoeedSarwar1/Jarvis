def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for w in word:
        for v in vowels:
            if w == v:
                count += 1

    return count


print(count_vowels("americano"))  # expected 5
