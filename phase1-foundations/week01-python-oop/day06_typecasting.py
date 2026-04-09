"""
Day 05 — Type casting
Phase 1, Week 1 | AI Learning Journey
Date: 9 April 2026

What I learned:
- recalling basics. (different types of conversion - int, str, list, tuple, set)

"""

my_num = 42
print(type(my_num))
my_str = str(my_num)
print(type(my_str), my_str)

str1 = "43"
num1 = int(str1)
print(type(num1), num1)

my_list = [23,"hello",2 , 6]
print(type(my_list))
my_tuple = tuple(my_list)
print(type(my_tuple), my_tuple)

list1 = [2,3,4,2,"hello"]
my_set = set(list1)
print(type(my_set), my_set)

str2 = "Hello good morning"
list3 = list(str2)
print(type(list3), list3)

