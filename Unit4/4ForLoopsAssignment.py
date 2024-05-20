# ========== 4.4.1 ==========

# word = input("Please type in a string: ")
# for letter in word:
#     print(letter)
#     print("*")

# # ========== 4.4.2 ==========

# number = int(input("Please type in a positive integer: "))
# num = number * -1
# for integer in range(num, number + 1):
#     if integer != 0:
#         print(integer)

# # ========== 4.4.3 ==========

# def list_of_stars(numbers):
#     for stars in numbers:
#         print("*" * stars)
# numbers = [3, 7, 1, 1, 2]
# list_of_stars(numbers)

# # ========== 4.4.4 ==========

# def palindromes(word):
#     word2 = ""
#     for letter in word:
#         word2 = letter + word2
#     if word == word2:
#         print(True)
#     else:
#         print(False)
# word = input("Please type in a word: ")
# palindromes(word)

# # ========== 4.4.5 ==========

# def sum_of_positives(numbers):
#     total = 0
#     for number in numbers:
#         if number > 0:
#             total += number
#     print(total)
# numbers = [1, -2, 3, -4, 5]
# sum_of_positives(numbers)

# # ========== 4.4.6 ==========

# def even_numbers(numbers):
#     even = []
#     for number in numbers:
#         if number % 2 == 0:
#             even.append(number)
#     print(even)
# numbers = [1, 2, 3, 4, 5]
# even_numbers(numbers)

# # ========== 4.4.7 ==========

# def list_sum(a, b):
#     sum_list = []
#     index = 0
#     for number in a:
#         sum = a[index] + b[index]
#         index += 1
#         sum_list.append(sum)
#     print(sum_list)
# a = [1, 2, 3]
# b = [7, 8, 9]
# list_sum(a, b)

# # ========== 4.4.8 ==========

def length_of_longest(my_list):
    total = 0
    longest = 0
    for word in my_list:
        total = len(word)
        if total > longest:
            longest = total
            total = 0
    return longest
my_list = ["first", "second", "fourth", "eleventh"]
result1 = length_of_longest(my_list)
print(result1)

# ========== 4.4.9 ==========

def length_of_shortest(my_list):
    shortest = "l" * result1
    for word in my_list:
        total = len(word)
        if total < len(shortest):
            shortest = word
    return shortest
my_list = ["first", "second", "fourth", "eleventh"]
result = length_of_shortest(my_list)
print(result)