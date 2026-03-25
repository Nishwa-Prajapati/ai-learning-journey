"""
Day 03 — Static method (decorator)
Phase 1, Week 1 | AI Learning Journey
Date: 25 March 2026

What I learned:
- inheritance : creating subclass that can override or completely new functionality without affecting the parent class

What was confusing:
- n/a
"""

class Employee:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname (self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    pass

Dev1 = Developer('Nishwa','Prajapati',7000)   #here developer class inherits Employee class's __init__
Dev2 = Employee('User','Test',8000)

print(Dev1.email)
print(Dev2.pay)