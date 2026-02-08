#Functions
#Function are nothing but a small programming unit in a big programming construct
#Functions are predefined(built-in) functions and user defined functions

#function

def main():
    print("Welcome to PythonRevision11")

main()

#function with argument
def greet(name):
    print(f"Hello, {name}!")

greet("Sid")

#function with return
def sum(a,b):
    c=a+b
    return c
a=10
b=12
print(sum(a,b))

#function calling
def func(name,age=24):
    print("Name:",name)
    print("Age:",age)
func("Sid",23)
func("Apollo")

