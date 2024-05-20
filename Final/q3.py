equation = input("Enter expression: ")

if equation[1] == "+":
    print(f"{equation[0]}{equation[1]}{equation[2]}=" + str(int(equation[0])+int(equation[2])))
elif equation[1] == "-":
    print(f"{equation[0]}{equation[1]}{equation[2]}=" + str(int(equation[0])-int(equation[2])))
elif equation[1] == "*":
    print(f"{equation[0]}{equation[1]}{equation[2]}=" + str(int(equation[0])*int(equation[2])))
else:
    print(f"{equation[0]}{equation[1]}{equation[2]}=" + str(float(equation[0])/float(equation[2])))