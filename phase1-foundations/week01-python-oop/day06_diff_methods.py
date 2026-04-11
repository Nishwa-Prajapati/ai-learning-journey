"""
Day 05 — Length and index
Phase 1, Week 1 | AI Learning Journey
Date: 9 April 2026

What I learned:
- recalling basics.

"""

# GET method
dict1 = {'Name' : 'Nishwa', 'Age' : 22, 'Hobby' : 'Cricket'}
my_dict = dict1.get('Age')
print("Age :", my_dict)

# set1 = {23,4,1,67}
# print(set1.get(1)) ->ERROR no such attribute 


# FIND method
str1 = "Hello, world!"
print(str1.find('world'))

str2 = "hello, hi, Hello, Hi, hello"
print(str2.find('h'))
print(str2.find(' '))
print(str2.find('H'))
print(str2.find('l'))

# COUNT method
my_list = [1,3,4,2,2,5,7,2,8,9,2]
print(my_list.count(2))

my_str = "Hello, hi, Hello, hello, hi, HIEEE"
print(my_str.count('h'))

# KEY, VALUES, ITEMS method

dict_items = {'apple' : 2, 'banana' : 3, 'orange' : 4}
print(dict_items.keys())
print(dict_items.values())
print(dict_items.items())

