"""
Day 03 — Dunder methods
Phase 1, Week 1 | AI Learning Journey
Date: 25 March 2026

What I learned:
- Usecase and different special methods and how they function
- enabling operator overloading and custom object behavior
- different special methods including comparisons, containers, arithmetic dunder methods and many more.

What was confusing:
- Whats the exact need and how they are applied?
"""

class Employee:

    raise_amount = 1.04

    def __init__ (self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__ (self):
        return f"Employee('{self.first}','{self.last}',{self.pay})"
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Nishwa','Prajapati',34000)
emp2 = Employee('User','Test',7800)

# print(emp1)
print(repr(emp1))     #repr() is just a wrapper which calls __repr__ behind the scenes
print(emp1.__repr__())
print(int.__add__(34,5))
# print(emp1 + emp2)   #gives error without dunder method __add__
print(emp1 + emp2)

print(len('test'))
# print(len(emp1))     #gives error without dunder method __len__
print(len(emp2))