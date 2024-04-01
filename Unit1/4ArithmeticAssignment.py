print("########## 1.4.1 ##########")
number = int(input("Please enter a number: "))
print(number*5)

print("########## 1.4.2 ##########")
name = input("What is your name: ")
year = int(input("Which year were you born: "))
print("Hi", name, "you will be", 2024-year, "years old at the end of the year 2024" )

print("########## 1.4.3 ##########")
days = int(input("How many days? "))
print("Seconds in that many days:", days*24*60*60)

print("########## 1.4.4 ##########")
# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)

print("########## 1.4.5 ##########")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
print("The sum of the numbers:", number1+number2)
print("The product of the numbers:", number1*number2)

print("########## 1.4.6 ##########")
sum = 0
number = int(input("Number: "))
sum += number
number = int(input("Number: "))
sum += number
number = int(input("Number: "))
sum += number
number = int(input("Number: "))
sum += number
print("The sum of the numbers is", sum, "and the mean is", sum/4)

print("########## 1.4.7 ##########")
eat = int(input("How many time a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much do you spend on groceries in a week? "))
sum = price*eat+groceries
print(" ")
print("Average food expenditure:")
print("Daily: $", sum/7)
print("Weekly: $", sum)