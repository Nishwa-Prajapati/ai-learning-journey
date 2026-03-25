"""
Day 03 — Static method (decorator)
Phase 1, Week 1 | AI Learning Journey
Date: 25 March 2026

What I learned:
- Multi subclass implementation
- use of isinstance and issubclass
- use of help function 

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

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

Dev1 = Developer('Nishwa','Prajapati',7000,'Java')   #here developer class inherits Employee class's __init__
Dev2 = Developer('Kush','Shah',2345,'Python')
Dev3 = Employee('User','Test',8000)

Mngr1 = Manager('Smith','Oza',4000,[Dev1,Dev3])
Mngr2 = Manager('Adam','Owal',3200,[])


# print(help(Developer))

print(Dev1.email)
print(Dev1.prog_lang)
print('Before raise :')
print(Dev1.pay)
print(Dev2.pay)
Dev1.apply_raise()
Dev2.apply_raise()
print('Dev1 pay raise by 10% :', Dev1.pay)
print('Dev2 pay raise by 4% :', Dev2.pay)

print('---------------------------------------')

print(Mngr1.email)
Mngr1.print_emp()
Mngr2.print_emp()

Mngr1.remove_emp(Dev1)
Mngr1.print_emp()

print('______*********_________')
print('---ISINSTANCE-----')
print(isinstance(Dev1,Developer))
print(isinstance(Dev2,Employee))
print(isinstance(Mngr1,Developer))

print('---ISSUBCLASS-----')
print(issubclass(Developer,Manager))
print(issubclass(Manager,Employee))