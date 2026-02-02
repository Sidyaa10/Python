#Class Functions
#Class Functions is functions in a class it can either modify objects in the class or give specific info about the object

from python28 import Student

student1 = Student("Sid","Computer Science",6.64)
student2 = Student("Apollo","Computer Science", 10)

print(student1.eligible_for_scholarship())
print(student2.eligible_for_scholarship())