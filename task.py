"""
    By defining the SchoolMember, Teacher, and Student classes in this way,
    we can create instances of each class and access their attributes and methods.
    We can also use inheritance to reuse the code of the SchoolMember class in the Teacher and Student classes,
    and override methods as needed in the child classes.
"""

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        return str()

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
    def show(self):
        SchoolMember.show(self)
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Student(SchoolMember):
    def __init__(self, name, age, grade):
        SchoolMember.__init__(self, name, age)
        self.grade = grade

    # Method that returns a string representation of a Teacher object
    # Overrides the show method in the parent class to include the salary attribute

    def show(self):
        SchoolMember.show(self)
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grade}"


