"""
Day 01 — Class and instance variable
Phase 1, Week 1 | AI Learning Journey
Date: 22 March 2026

What I learned:
- Difference between class and instance variable. Might me here it is not exactly shown but,
- Class variables that are shared among all instances of the class
- instance variables can be unique for each instance like name, age, grade etc.
- Use of __dict__ 

What was confusing:
- Why we cant access class variables through instance variables ?
"""


class Student:

    no_of_student = 0

    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.no_of_student += 1

    def introduce(self):
        print(f'{self.name} got {self.grade} at the age of {self.age} .') 

    def is_passing(self):
        return self.grade>=60
    

print(Student.no_of_student) 
Student1 = Student('Raj',14,75)
Student2 = Student('Mehul',15,50)
Student3 = Student('Preeti',14,60)
print(Student.no_of_student)

# Student1.introduce()      --> individual calling
# print(Student1.is_passing())

students = [Student1,Student2,Student3]    # calling all together

for student in students:
    student.introduce()
    print(student.is_passing())
    print()