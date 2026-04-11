"""
Day 05 — More methods for list, tuple, set, dictionaries
Phase 1, Week 1 | AI Learning Journey
Date: 11 April 2026

What I learned:
- recalling basics. (different attributes : extend, insert, )

"""

my_list = [1,2,3,"bye"]
print("List elements :", my_list)
# new_list = my_list.extend(["hieee", 34]) -> doesnt work , it outputs "None"
my_list.extend(["hieee", 34])
print("New extended list :", my_list) # append only take 1 arguement 

# my_tuple = ('Strawberry', 77, "Apple", 90)  -> tuple has no attribute insert
# my_tuple.insert(0,45.67)
# print("Inserted new element :", my_tuple)

# INSERT ELEMENT -> ADDS element not REPLACE it
my_list2 = ["Apple", 67.89, 89, 11, "Hello"]
my_list2.insert(0, "34")
print("Inserted new element in list : ", my_list2)


# SET DEFAULT -> returns the key's value which is set default or else mentioned string

my_default = {'Name' : 'Nishwa', 'Age' : 45, 'B' : '34.6'}
set_default_value = my_default.setdefault('B', "B not present")
print(set_default_value)

print_default_value = my_default.setdefault('C', "C not present")
print(print_default_value)

