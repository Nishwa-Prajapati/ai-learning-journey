"""
Day 02 — Class method (decorator)
Phase 1, Week 1 | AI Learning Journey
Date: 24 March 2026

What I learned:
- Slight different usage of class method here 

What was confusing:
- Why are we exactl doing this ?
"""

# class method as an alternative constructor (split by -)

class Employee:
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        # pass
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)



emp_str1='Nishwa-Prajapati-70'
emp_str2='User-Test-60'
emp_str3='Khushi-Patel-23'

# first, last, pay = emp_str1.split('-')       without class method 
# new_empstr = Employee(first,last,pay)

# print(new_empstr.email)

new_empstr= Employee.from_string(emp_str1)     #using class method
print(new_empstr.email)

