"""
Day 02 — Static method (decorator)
Phase 1, Week 1 | AI Learning Journey
Date: 24 March 2026

What I learned:
- @staticmethod (decorator )usage
- Got no such specific common convention 
- importing modules

What was confusing:
- how this weekdays are inbuild set from 0 to 6?
"""


import datetime

class CheckDay:

    @staticmethod # has no common convention means for regular methos its 'self and for class method its 'cls' 
    def is_workday(day):
        # if day.weekday() in (5,6):    -> calling weekday method on datetime object and passing the tuple here where 5 is saturday and 6 is sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
my_date1 = datetime.date(2026,8,12)
my_date2 = datetime.date(2024,2,18)
print(CheckDay.is_workday(my_date1))
print(CheckDay.is_workday(my_date2))


