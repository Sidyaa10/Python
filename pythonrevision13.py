#Exception Handling

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

print("Another example")
try:
    x = 10 / 0
except:
    print("Something went wrong!")