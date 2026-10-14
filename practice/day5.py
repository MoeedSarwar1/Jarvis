
# Question 1: Find the Bigger Number

def bigger(number1, number2):
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    elif number1 == number2:
        return number2


print("Question 1: Find the Bigger Number")
print("bigger(3, 7):", bigger(3, 7))
print("bigger(9, 2):", bigger(9, 2))
print("bigger(4, 4):", bigger(4, 4))
print("bigger(3, 7) + 1:", bigger(3, 7) + 1)


# Question 2: Grade a Score

def grade(score):
    if score < 50:
        return "fail"
    elif score >= 50 and score < 80:
        return "pass"
    else:
        return "distinction"


print("\nQuestion 2: Grade a Score")
print("grade(30):", grade(30))
print("grade(49):", grade(49))
print("grade(50):", grade(50))
print("grade(79):", grade(79))
print("grade(79.99):", grade(79.99))
print("grade(80):", grade(80))
print("grade(100):", grade(100))
print("grade(49.5):", grade(49.5))


# Question 3: Sum Numbers from 1 to n

def sum_to(n):
    total = 0

    while n > 0:
        total = total + n
        n = n - 1

    return total


print("\nQuestion 3: Sum Numbers from 1 to n")
print("sum_to(5):", sum_to(5))
print("sum_to(10):", sum_to(10))
print("sum_to(1):", sum_to(1))
print("sum_to(0):", sum_to(0))


# Question 4: Add Two Numbers Safely

def safe_add(a, b):
    a = int(a)
    b = int(b)

    return a + b


print("\nQuestion 4: Add Two Numbers Safely")
print('safe_add("3", "4"):', safe_add("3", "4"))
print('safe_add("10", "0"):', safe_add("10", "0"))
print('safe_add("0", "0"):', safe_add("0", "0"))
print('safe_add("0", "5"):', safe_add("0", "5"))
print('safe_add("3", "4") + 1:', safe_add("3", "4") + 1)
