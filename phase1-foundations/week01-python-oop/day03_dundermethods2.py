class Student:

    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f'{self.name} got {self.grade} at the age of {self.age} .') 

    def is_passing(self):
        return self.grade>=60

class Gradstudent(Student):

    def __init__(self,name,age,grade,advisor):
        super().__init__(name,age,grade) 
        self.advisor = advisor

    def __str__(self):
        return f'{self.name} : Advisor {self.advisor}'  

class Classroom():

    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def __len__(self):
        return len(self.students)
    
    def __iter__(self):
        return iter(self.students)

s1 = Student("Nishwa", 20, 85)
s2 = Student("Raj", 19, 78)
g1 = Gradstudent("Amit", 24, 90, "Dr. Sharma")

classroom = Classroom()
classroom.add_student(s1)
classroom.add_student(s2)
classroom.add_student(g1)


print(s1)
print(g1)

print("Total students:", len(classroom))

for student in classroom:
    print(student)