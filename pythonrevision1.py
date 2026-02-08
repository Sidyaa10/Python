#Operators in python

#Comparison Operators
print("Comparison Operator")
x=10
y=30
print(x<y)
print(x>y)
print(x!=y) #not equal to

#Assignment Operators

print("Assignment Operator")
a=20
b=30
a+=b
print(a)
x=40
x*=y
print(x)
a=10
b=20
a-=b
print(a)

#Bitwise Operator

print("Bitwise Operator")
x=240
y=1
z=x|y
print(z)
a=x&y
print(a)
b=x^y
print(b)

#Logical Operator

print("Logical Operator")
#and operator return true if both sides are correct
a=1>4 and 2<3
print(a)
#or operator returns true if any one side is true
b=1>4 or 2<3
print(b)
#not operator returns true statement as false
c=not(4>1)
print(c)