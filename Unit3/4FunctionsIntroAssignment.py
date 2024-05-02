# ========== 3.4.1 ==========

def seven_dwarves():
    print("Bashful")
    print("Doc")
    print("Dopey")
    print("Grumpy")
    print("Happy")
    print("Sleepy")
    print("Sneezy")

seven_dwarves()

# ========== 3.4.2 ==========

def first_character():
    print("python"[0:1])
    print("yellow"[0:1])
    print("tomorrow"[0:1])
    print("heliotrope"[0:1])
    print("open"[0:1])
    print("night"[0:1])

first_character()

# ========== 3.4.3 ==========

def mean(n1, n2, n3):
    print((n1 + n2 + n3)/3)

mean(5, 3, 1)
mean(10, 1, 1)

# ========== 3.4.4 ==========

def print_many_times(text, num):
    while num > 0:
        print(text)
        num = num-1
text = input("string: ")
num = int(input("times:"))
print_many_times(text, num)

# ========== 3.4.5 ==========

def hash_square(num):
    total = 0
    while True:
        print("#" * num)
        total = total + 1
        if total == num:
            break
num = int(input("Number: "))
hash_square(num)

# ========== 3.4.6 ==========

def chessboard(num):
    total = 0
    while True:
        if num % 2 == 0:
            print("10" * (num // 2))
            print("01" * (num // 2))
            total = total + 1
            if total == (num // 2):
                break
        else:
            print("10" * (num // 2) + "1")
            print("01" * (num // 2) + "0")
            total = total + 1
            if total == (num // 2):
                print("10" * (num // 2) + "1")
                break
num = int(input("Number: "))
chessboard(num)