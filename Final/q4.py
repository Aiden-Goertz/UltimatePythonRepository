def scrabble_score(word):
    score = 0
    for letter in word:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "l" or letter == "n" or letter == "s" or letter == "t" or letter == "r":
            score += 1
        elif letter == "d" or letter == "g":
            score += 2
        elif letter == "b" or letter == "c" or letter == "m" or letter == "p":
            score += 3
        elif letter == "f" or letter == "h" or letter == "v" or letter == "w" or letter == "y":
            score +=4
        elif letter == "k":
            score += 5
        elif letter == "j" or letter == "x":
            score += 8
        else:
            score += 10
    print(score)
word = input("Please tpye in a word: ")
scrabble_score(word)