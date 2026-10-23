def longest_word(words):
    word = words[0]
    for n in words:
        if len(n) > len(word):
            word = n

    return word

print(longest_word(["ali", "kashannn", "jamal"])) #expected kashannn


def count_letter(word, target):
    count = 0
    for w in word:
        if w == target:
            count += 1


    return count

print(count_letter("banana","a")) #expected: 3


def word_lengths(words):
    counts = {}
    for w in words:
        counts[w] =  len(w)
    return counts

print(word_lengths(["go", "tea","go","duffer"])) #expected: {"go": 2, "tea": 3}
