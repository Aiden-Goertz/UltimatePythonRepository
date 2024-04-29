# ========== 3.3.1 ==========

word = input("Please type in a string: ")
num1 = 0
num2 = 0
while True:
    print(word[num1:num2])
    num2 = num2 + 1
    if num2 == len(word) + 1:
        break

# ========== 3.3.2 ==========

word = input("Please type in a string: ")
num1 = len(word)
while True:
    print(word[num1:])
    num1 = num1 - 1
    if num1 < 0:
        break

# ========== 3.3.3 ==========

word = input("Please type in a string: ")
let1 = ("a" in word)
let2 = ("e" in word)
let3 = ("o" in word)
if let1 == True:
    print("a found")
else:
    print("a not found")
if let2 == True:
    print("e found")
else:
    print("e not found")
if let3 == True:
    print("o found")
else:
    print("o not found")

# ========== 3.3.4 ==========

word = input("Please type in a word: ")
let = input("Please type in a character: ")
let1 = (word.find (let))
if let1 + 3 > len(word) + 1:
    print("")
else:
    print(word[let1:let1+3])

# ========== 3.3.5 ==========

word = input("Please type in a word: ")
let = input("Please type in a character: ")
while True:
    num = (word.find (let))
    if len(word) <= 3:
        break
    else:
        print(word[num:num+3])
        word = word[num+1:]

# ========== 3.3.6 ==========

string = input("Please type in a string: ")
sub = input("Please type in a substring: ")
pos = string.find(sub)
num = pos
if pos >= 0:
    string = string[pos + 1:]
    pos = string.find(sub)
    num = num+pos
    if pos >= 0:
        print("The second occurrence of the substring is at index", num + 1, ".")
    else:
        print("The substring does not occur twice.")
else:
    print("The substring does not occur twice.")