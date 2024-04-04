
print("########## 1.5.1 ##########")
number = int(input("Please type a number: "))
if number == 1984:
    print("Orwell")

print("########## 1.5.2 ##########")
number = int(input("Please type in a number: "))
if number < 0:
    print("The absolute value of this number is", number*-1)
if number > 0:
    print("The absolute value of this number is", number)
if number == 0:
    print("The absolute value of this number is 0")

print("########## 1.5.3 ##########")
name = input("What is your name? ")
if name != "Jerry":
    soup = int(input("How many portions of soup? "))
    print("The total cost is", soup*5.9)
print("Next please!")

print("########## 1.5.4 ##########")
number = int(input("Type in a number: "))
if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")
print("Thank you!")

print("########## 1.5.5 ##########")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")
if operation == "add":
    print(number1, "+", number2, "=", number1+number2)
if operation == "subtract":
    print(number1, "-", number2, "=", number1-number2)
if operation == "multiply":
    print(number1, "*", number2, "=", number1*number2)
if operation == "divide":
    print(number1, "/", number2, "=", number1/number2)

print("########## 1.5.6 ##########")
temp = int(input("Type in a temperature: "))
print(temp, "degrees Fahrenheit equals", (temp-32)*(5/9), "degrees Celsius")
if (temp-32)*(5/9) <= 0:
    print("Brr! It's cold in here!")

print("########## 1.5.7 ##########")
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = input("Day of the week: ")
if day == "sunday":
    print("Daily wages:", wage*hours*2)
if day != "sunday":
    print("Daily wages:", wage*hours)

print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")
    print("You now have", points, "points")
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
    print("You now have", points, "points")

print("########## 1.5.9 ##########")
print("What is the weather forcast for tomorrow?")
temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if temp < 20:
    print("I recommned a sweater as well")
if temp < 10:
    print("Take a jacket with you")
if temp < 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")