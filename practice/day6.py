# Question 1
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[2])
print(len(fruits))
fruits.append("mango")
print(len(fruits))
print(fruits)


# Question 2

nums = [10, 20, 30]
print(nums[1])
nums.append(40)
print(nums[len(nums) - 1])
# print(nums[4])


# Question 3

scores = [3, 8, 5]
total = 0
for s in scores:
    total = total + s
    print("added", s, "total now", total)
print("final", total)


# Question 4

letters = ["c", "a", "t"]
word = ""  # before

for ch in letters:     # loops job
    word = word + ch  # inside
    # after
print(word)


# Question 5


def count_long(words):
    long_words = []
    for word in words:
        if len(word) > 3:
            long_words.append(word)
    return len(long_words)


x = count_long(["princess", "jaadu", "ab"])
print(x)
y = count_long(["hello"])
print(y)
print(count_long(["cat", "dog"]))   # expected: 0
print(count_long([]))               # expected: 0
