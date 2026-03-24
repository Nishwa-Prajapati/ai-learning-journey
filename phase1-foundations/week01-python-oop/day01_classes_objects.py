"""
Day 01 — Classes and objects
Phase 1, Week 1 | AI Learning Journey
Date: 22 March 2026

What I learned:
- defining class and objects
- __init__ constructor

What was confusing:
- How this different return statement works
"""


class Employee:
    def __init__(self,first,last,pay):
        self.fname = first    #self.first=first
        self.lname = last     #self.last=last
        self.salary = pay     #self.pay=pay
        self.mmail = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
        # return f'{self.fname} is rich!'

emp1 = Employee('Nishwa','Prajapati',50000)
emp2 = Employee('Test','User',60000)

emp1.fullname()    #works same as the below print 
print(Employee.fullname(emp1))
print(f"{emp1.fname} {emp1.lname} has salary of {emp1.salary}.")