"""
Day 01 — Class and instance vraibale
Phase 1, Week 1 | AI Learning Journey
Date: 22 March 2026

What I learned:
- defining class and objects
- __init__ constructor

What was confusing:
- How this different return statement works
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