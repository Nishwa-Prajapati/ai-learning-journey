"""
Day 03 — Static method (decorator)
Phase 1, Week 1 | AI Learning Journey
Date: 25 March 2026

What I learned:
- Property decorator -> @property , @____.setter and @___.deleter
- how to use a method as an attribut and not using parathesis at the end
- how to make quick change without deleting or making changes all over the place on code

"""

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Name deleted!!!!!")
        self.first = None
        self.last = None
    
emp1 = Employee('Nishwa','Prajapati',4000)

emp1.first = 'Corey' #but wont change the first name in email without getter or setter here so add email as getter 
emp1.fullname = 'Luv Oza'

print(emp1.first)
print(emp1.email) #now the email is changed but what if i want to set new full name and it should also be reflected to first and last name and email so use setter
print(emp1.fullname)

#after changed fullname and impacting everywhere, what if i want to delet the fullname -> use deleter

del emp1.fullname

print(emp1.fullname)