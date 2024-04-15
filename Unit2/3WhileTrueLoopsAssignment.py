# ========== 2.3.1 ==========

# input()
# while True:
#     word = input("Shall we continue? ")
   
#     if word == "no":
#         print("okay then")
#         break
#     print("hi")

# ========== 2.3.2 ==========

# from math import sqrt
# while True:
#     num = int(input("please type in a number: "))
#     if num < 0:
#         print("invald number")
#     elif num == 0:
#         print("Exiting")
#         break
#     else:
#         print(sqrt(num))

# ========== 2.3.3 ==========

# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number == 0:
#     break

# print("Now!")

# ========== 2.3.4 ==========

# password = input("Password: ")
# while True:
#     word = (input("Repeat Password: "))
#     if password == word:
#         print("User account created!")
#         break
#     else:
#         print("They do not match")

# ========== 2.3.5 ==========

# atp = 0

# while True:
#     pin = int(4321)
#     PIN = int(input("PIN: "))
#     atp = atp + 1    
#     if PIN == pin and atp == 1:
#         print("Correct! It took you a single attempt!")
#         break
#     elif PIN == pin:
#         print("Correct! It took you", atp, "attempts!")
#         break
#     else:
#         print("Wrong")

# ========== 2.3.6 ==========

# year = int(input("Year: "))
# leap = year + 1
# while True:
#     if leap % 4 == 0:
#         print("The next leap year after", year, "is", leap)
#         break
#     else:
#         leap = leap + 1

# ========== 2.3.7 ==========

# word = input("Please type in a word: ")
# sent = word + " "
# while True:
#     word = input("Please type in a word: ")
#     if word == "end":
#         print(sent)
#         break
#     else:
#        sent = sent + word + " " 

# ========== 2.3.8 ==========

# word = input("Please type in a word: ")
# sent = word + " "
# word2 = word
# while True:
#     word = input("Please type in a word: ")
#     if word == "end" or word == word2:
#         print(sent)
#         break
#     else:
#        sent = sent + word + " "
#        word2 = word 

# ========== 2.3.9 ==========

print("Please type in integer numbers. Type in 0 to finish.")
total = 0
sum = 0
pos = 0
neg = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    else:
        total = total + 1
        sum = number + sum
        if number < 0:
            neg = neg + 1
        else:
            pos = pos + 1
print("Numbers typed in:", total)
print("Sum of numbers:", sum)
print("Mean of number:", sum/total)
print("Positive numbers:", pos)
print("Negative numbers:", neg)