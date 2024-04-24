# ========== 3.2.1 ==========

word = input("Please type in a string: ")
num = int(input("Please type in an amount: "))
print(word * num)

#  ========== 3.2.2 ==========

word1 = input("Please type in string 1: ")
word2 = input("Please type in string 2: ")
if len(word1) > len(word2):
    print(word1, "is longer")
elif len(word2) > len(word1):
    print(word2, "is longer")
else:
    print("The strings are equally long")

# ========== 3.2.3 ==========

word = input("Please type in a string: ")
num1 = len(word)
num = len(word)
total = 0
while total < num1:
    num = num - 1
    print(word[num])
    total = total + 1
    if total == num1:
        break

# ========== 3.2.4 ==========

word = input("Please type in a string: ")
if word[1] == word[-2]:
    print("The second and the second to last characters are", word[1])
else:
    print("The second and the second to last characters are different")

# ========== 3.2.5 ==========

num = int(input("Width: "))
print("#" * num)

# ========== 3.2.6 ==========

width = int(input("Width: "))
height = int(input("Height: "))
num = height
while True:
    print("#" * width)
    num = num - 1
    if num == 0:
        break

# ========== 3.2.7 ==========

while True:
    sent = input("Please type in a string: ")
    print(sent)
    print("-" * len(sent))
    if sent == "":
        break

# ========== 3.2.8 ==========

word = input("Please type in a string: ")
length = len(word)
print(("*" * (20 - length)) + word)

# ========== 3.2.9 ==========

word = input("Word: ")
length = len(word)
open = 28 - length
print("*" * 30)
if length%2 == 0:
    print("*" + open//2 * " " + word + open//2 * " " + "*")
else:
    print("*" + open//2 * " " + word + (open//2 + 1) * " " + "*")
print("*" * 30)