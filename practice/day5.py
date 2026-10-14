# Write a function bigger(a, b) that takes two numbers and returns the larger one. If they’re equal, return either.

def bigger(number1, number2):
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    elif number1 == number2:
        return number2


print(bigger(3, 7))
print(bigger(9, 2))
print(bigger(4, 4))
print(bigger(3, 7) + 1)


print("Question 2 Grading")
# Write a function grade(score) that takes a score and returns its grade as a piece of text.

# Rules
#
# A score below 50 is "fail".
# A score of at least 50 and below 80 is "pass".
# A score of 80 or more is "distinction".
#
# Every score gets exactly one grade. There are no gaps between the ranges.
#
# Input: score, a number from 0 to 100. It may have a decimal point, like 79.99.
#
# Output: exactly one of "fail", "pass" or "distinction", all lowercase.


def grade(score):
    if score < 50:
        return 'fail'
    elif score >= 50 and score < 80:
        return 'pass'
    else:
        return 'distinction'


print(grade(30))
print(grade(49))
print(grade(50))
print(grade(79))
print(grade(79.99))
print(grade(80))
print(grade(100))
print(grade(49.5))
