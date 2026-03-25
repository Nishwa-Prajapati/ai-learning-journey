"""
Day 03 — Static method (decorator)
Phase 1, Week 1 | AI Learning Journey
Date: 25 March 2026

What I learned:
- inheritance application
- use of super keyword

What was confusing:
- how super exactly works
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

    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

Dev1 = Developer('Nishwa','Prajapati',7000,'Java')   #here developer class inherits Employee class's __init__
Dev2 = Employee('User','Test',8000)

print(Dev1.email)
print(Dev1.prog_lang)
print('Before raise :')
print(Dev1.pay)
print(Dev2.pay)
Dev1.apply_raise()
Dev2.apply_raise()
print('Dev1 pay raise by 10% :', Dev1.pay)
print('Dev2 pay raise by 4% :', Dev2.pay)


