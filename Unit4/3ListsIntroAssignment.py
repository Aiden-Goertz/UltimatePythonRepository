# ========== 4.3.1 ==========

list = [10, 2, 3, 4, 5]
while True:
    index = int(input("Please type in an index: "))
    if index == -1:
        break
    else:
        value = int(input("Please type in a new value: "))
        list.pop(index)
        list.insert(index, value)
        print(list)

# ========== 4.3.2 ==========

number = []
items = int(input("How many items: "))
total = 1
while True:
    n1 = int(input(f"Item {total}: "))
    number.append(n1)
    total += 1
    if total > items:
        break
print(number)

# ========== 4.3.3 ==========

numbers = []
total = 1
while True:
    print("The list is now", numbers)
    edit = input("a(d)d, (r)emove or e(x)it: ")
    if edit == "d":
        numbers.append(total)
        total += 1
    elif edit == "r":
        numbers.remove(len(numbers))
        total -= 1
    else:
        break
print("Bye!")

# ========== 4.3.4 ==========

numbers = []
total = -1
while True:
    word = input("Word: ")
    total +=1
    if word in numbers:
        break
    numbers.append(word)
print("You typed in", total, "different words")