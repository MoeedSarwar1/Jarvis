
def total(numbers):
    sum_of_integers = 0
    for n in numbers:
        sum_of_integers = sum_of_integers + n
    return sum_of_integers


print(total([1, 2, 3]))  # expected 6
print(total([]))  # expected 0
print(total([-1, -2, 2]))  # expected -1


def biggest(numbers):
    biggest_so_far = numbers[0]
    for n in numbers:
        if n > biggest_so_far:
            biggest_so_far = n

    return biggest_so_far


print(biggest([1, 2, 3]))  # expected 3
print(biggest([-2, 3, -10]))  # expected 3
print(biggest([-2, 0, -1]))  # expected 0
print(biggest([-2, -5, -9]))  # expected -2
