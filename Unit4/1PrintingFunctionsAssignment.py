# ========== 4.1.1 ==========

def line(num, let):
    if let == "":
        print("*" * num)
    else:
        print(let[0] * num)
num = int(input("Number: "))
let = input("Letter: ")
line(num, let)

# ========== 4.1.2 ==========

def box_of_hashes(height):
    count = 0
    while True:
        line(10, "#")
        count += 1
        if count >= height:
            break
height = int(input("Height: "))
box_of_hashes(height)

# ========== 4.1.3 ==========

def square_of_hashes(num):
    count = 0
    while True:
        line(num, "#")
        count += 1
        if count >= num:
            break
num = int(input("Number: "))
square_of_hashes(num)

# ========== 4.1.4 ==========

def square(num, let):
    count = 0
    while True:
        line(num, let)
        count += 1
        if count >= num:
            break
num = int(input("number: "))
let = input("Letter: ")
square(num, let)

# ========== 4.1.5 ==========

def triangle(base):
    count = 0
    num = 1
    while True:
        line(num, "#")
        num += 1
        count += 1
        if count >= base:
            break
base = int(input("Base:"))
triangle(base)

# ========== 4.1.6 ==========

def shape(num1, let1, num2, let2):
    count = 1
    while count < num1 + 1:
        line(count, let1)
        count += 1
    count = 0
    while count < num2:
        line(num1, let2)
        count += 1
num1 = int(input("Number 1: "))
let1 = (input("Letter 1: "))
num2 = int(input("Number 2: "))
let2 = (input("Letter 2: "))
shape(num1, let1, num2, let2)

# ========== 4.1.7 ==========

def spruce(width):
    count = 0
    amount = 1
    space = width
    print("a spruce!")
    while count < width:
        print(" " * (space-1), "*" * amount)
        amount += 2
        count += 1
        space -= 1
    print(" " * (width-1), "*")
width = int(input("Width: "))
spruce(width)