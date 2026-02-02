#Make a calculator using if and else statements

num = float(input("Enter first number: "))
op= input("Enter a operator: ")
num1 = float(input("Enter second number: "))

if op == "+":
    print(num+num1)
elif op =="-":
    print(num-num1)
elif op =="*":
    print(num*num1)
elif op =="/":
    print(num/num1)
else:
    print("Operation not supported")
