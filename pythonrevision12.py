#Scope of variables
#local and global variable

#Global variable can be used anywhere throughout the program
#Local variable is only available in a certain code block of the program

print("Global Variable")
x = 10  # global variable

def my_function():
    y = 20  # local variable
    print(f"Inside function: x = {x}, y = {y}")

my_function()
print(f"Outside function: x = {x}")
# print(y)  # This would give an error because y is not defined here


print("Local Variable")