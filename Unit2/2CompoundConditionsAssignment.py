# print("########## 2.2.1 ##########")

age = int(input("What is your age? "))
if age > 5:
    print("Ok, you're", age, "years old")
elif age <= 5 and age >= 0:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")

# print("########## 2.2.2 ##########")
    
name = input("Please type in your name: ")
if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

# print("########## 2.2.3 ##########")

grade = float(input("Type in a percent: "))
if grade > 100 or grade < 0:
    print("Grade: impossible!")
elif grade <= 100 and grade >= 90:
    print("Grade: A")
elif grade < 90 and grade >= 80:
    print("Grade: B")
elif grade < 80 and grade >= 70:
    print("Grade: C")
elif grade < 70 and grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# print("########## 2.2.4 ##########")

number = int(input("Number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")


# print("########## 2.2.5 ##########")

year = int(input("Please type a year: "))
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("That year is a leap year.")
elif year % 4 == 0 and year % 100 == 0:
    print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year")

# print("########## 2.2.6 ##########")

let1 = input("1st letter: ")
let2 = input("2nd letter: ")
let3 = input("3rd letter: ")
if let1 > let2 and let1 < let3 or let1 < let2 and let1 > let3:
    print("The letter in the middle is", let1)
elif let2 > let1 and let2 < let3 or let2 < let1 and let2 >let3:
    print("The letter in the middle is", let2)
else:
    print("The letter in the middle is", let3)