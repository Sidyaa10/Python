class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


    def eligible_for_scholarship(self):
        if self.gpa >= 8.0:
            return True
        else:
            return False