#Try Except Block

try:
    value= 10/0
    number = int(input("Enter a number:"))
    print(number)
except ZeroDivisionError:
    print("Not Divisible by 0")
except ValueError:
    print("Invalid Input")
