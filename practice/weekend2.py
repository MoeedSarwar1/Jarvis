def smallest(numbers):
    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


print(smallest([1, 2, 3, 4, 56]))  # expected 1
print(smallest([11, 2, 3, 4, 56]))  # expected 2
print(smallest([111, 22, 33, 4, 56]))  # expected 4


def count_above(numbers, limit):
    bigger_number = 0
    for n in numbers:
        if n > limit:
            bigger_number += 1

    return bigger_number


print(count_above([1, 2, 3, 4, 56], 1))  # expected 4


def find_slot(numbers, target):
    slot = 0
    for n in numbers:
        if n == target:
            return slot
        else:
            slot += 1
    return -1


print(find_slot([1, 23, 32, 4, 3], 3))  # expected 4


def second_largest(numbers):
    biggest = numbers[0]
    second = smallest(numbers)
    for n in numbers:
        if n > biggest:
            biggest = n
    for n in numbers:
        if n < biggest and n > second:
            second = n

    return second


print(second_largest([9, 7, 2]))  # 7
print(second_largest([4, 9, 2, 7]))  # 7
print(second_largest([5, 5, 3]))  # 3
