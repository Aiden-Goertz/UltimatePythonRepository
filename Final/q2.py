due = 50

while True:
    print(f"Amount due: {due}")
    coin = int(input("Insert coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        due -= coin
        if due <= 0:
            print(f"Change Owed: {due * -1}")
            break
    else:
        print("Error - this coin type not accepted")
    