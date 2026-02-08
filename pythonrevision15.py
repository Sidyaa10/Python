#Classes and objects
#Object Oriented Programming
#Object oriented programming was able to solve many procedural programming problems

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog('Buddy', 3)
my_dog.bark()  # Output: Buddy says Woof!
print(my_dog.age)  # Output: 3


#Class variables
#The class variables are sharable among all the instances of the class
class Dog:
    species = 'Canine'  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

print(Dog.species)  # Output: Canine

d1 = Dog('Buddy')
d2 = Dog('Max')
print("Buddy's species is " +d1.species)  # Output: Canine
print("Max's species is "+d2.species)  # Output: Canine


#Class Inheritance
#The class inheritance allows us to inherit methods and attributes of the parent class and access them as one of their own

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog('Buddy')
my_dog.eat()   # Output: Buddy is eating.
my_dog.bark()  # Output: Buddy says Woof!