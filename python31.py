#Inheritance
#Inheritance is where we can define a bunch of functions or attributes inside of a class, and then we can use those functions or attributes in an another class, without writing them again.

from python30 import Chef
from python32 import ItalianChef

myChef = Chef()
myChef.make_salad()

myItalianChef = ItalianChef()
myItalianChef.make_chicken()
myItalianChef.make_salad()