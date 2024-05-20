first_name = input("Please type in your first name: ")
last_name = input("Please type in your Last name: ")
gpa = float(input("Please type in your current GPA: "))

def score(gpa):
    if gpa >= 3.86:
        scholarship = 16000
    elif gpa >= 3.7:
        scholarship = 12000
    elif gpa >= 3.5:
        scholarship = 8000
    elif gpa >= 3.25:
        scholarship = 4000
    else:
        scholarship = 0
    return scholarship
total = score(gpa)

if last_name[0] <= "K" or last_name[0] <= "k":
    print(f"Hello {first_name}. You should report to school on Monday and Thursday. You are eligibile for a scholarship of ${total}.")
else:
    print(f"Hello {first_name}. You should report to school on Tuesday and Friday. You are eligibile for a scholarship of ${total}.")
