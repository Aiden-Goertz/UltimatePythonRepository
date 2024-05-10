# ========== 4.2.1 ==========

def greatest_number(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    else:
        return n3
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
greatest = greatest_number(n1, n2, n3)
print("The greatest number is", greatest)

# ========== 4.2.2 ==========

def same_chars(word, n1, n2):
    if word[n1] == word[n2] or word[n2] == word[n1]:
        return True
    else:
        return False
word = input("Please type a string: ")
n1 = int(input("Please type in a index: "))
n2 = int(input("Please type in a index: "))
answer = same_chars(word, n1, n2)
print(answer)

# ========== 4.2.3 ==========

sent = input("Please type in a sentence: ")
def first_word(sent):
    place = ""
    index = 0
    while True:
        if sent[index] == " ":
            break
        else:
            place = place + sent[index]
            index = index + 1
    return place
first = first_word(sent)
def second_word(sent):
    place = ""
    index = 0
    while True:
        if sent[index] == " ":
            if first == place:
                index += 1
                place = ""
            else:
                break
        else:
            place = place + sent[index]
            index = index + 1
    return place
second = second_word(sent)
def last_word(sent):
    place = ""
    index = len(sent)-1
    while True:
        if sent[index] == " ":
            break
        else:
            place = sent[index] + place
            index -= 1
    return place
last = last_word(sent)
print(first)
print(second)
print(last)