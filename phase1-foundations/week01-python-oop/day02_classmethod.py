class Employee:
    no_of_emp = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emp += 1

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

print('No. of employee BEFORE INSTANCE:',Employee.no_of_emp)

emp1 = Employee('Nishwa','Prajapati',50000)
emp2 = Employee('User','Test',7000)

print('No. of employee AFTER INSTANCE:',Employee.no_of_emp)

Employee.set_raise_amt(1.05)      #Employee.apply_raise(1.05) gives error as its an instance method and not class method so it expects to be employe object there and not 1.05
print(emp1.raise_amount)          # we need to add class method to solve this issue 
print(emp2.raise_amount)
print(Employee.raise_amount)
