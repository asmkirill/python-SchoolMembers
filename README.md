# SchoolMembers

Quite common task for Python students.

Write a program that defines a "SchoolMember" class to represent individuals in a school. 
"Teacher" and "Student" are subclasses of "SchoolMember" with similar interfaces, each having a public show() method. 

The "Teacher" class takes three parameters: 
name (a string), age (an integer), and salary (an integer).
The "Student" class takes: name, age, and grades. 

The "SchoolMember" class should contain the initialization logic for both subclasses.

Method `show()` returns string:

>>> persons = [Teacher("Ms.Godvin", 45, 4000), Student("Samuel", 19, 88)]
