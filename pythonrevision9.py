#Loops

#If and if else statements

password = input("Enter the password:")
if password == "MI6":
    print("Welcome Agent 007")
else:
    print("Incorrect Password, Access Denied")

#if, elif and else statements

cgpa = float(input("Enter your CGPA: "))
if cgpa < 5:
    print("You have failed your exams")
elif cgpa < 7:
    print("You are not eligible for a scholarship")
elif cgpa >= 7:
    print("You are eligible for a scholarship")
else:
    print("You are not a graduate")