def sum_above(numbers, limit):
    sum_of_numbers = 0
    for n in numbers:
        if n > limit:
            sum_of_numbers = sum_of_numbers + n
    return sum_of_numbers


print(sum_above([1, 5, 6], 4))  # expected 11


def remove_letter(text, letter):
    removed_letter = ""
    for n in text:
        if n != letter:
            removed_letter += n
    return removed_letter


print(remove_letter("banana", "a"))  # expected bnn
print(remove_letter(" ", "a"))  # expected " "


def count_by_length(words):
    counts = {}
    for a in words:
        counts[len(a)] = counts.get(len(a), 0) + 1

    return counts


print(count_by_length(["hi", "ok", "cat", "hi"]))  # expected {"2":3, "3":1}
