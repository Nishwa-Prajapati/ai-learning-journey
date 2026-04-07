"""
Day 05 — Arithmetic Operators
Phase 1, Week 1 | AI Learning Journey
Date: 7 April 2026

What I learned:
- recalling basics. (Concating list, string and COPY DICTIONARY)

"""

# CONCATING LIST
list1 = [1,2,3,4]
list2 = ["hello", "Nishwa"]
result = list1 + list2
print(result)

conclude = list1 * 2
print(conclude)


# CONCATING STRING
string1 = "Hello"
string2 = "World"
adding_string = string1 + string2
add_string = string1 + " " + string2
print(adding_string)
print(add_string)

word = "Spam"
answer = word * 4
print(answer)

# COPY DICTIONARY
dict1 = {'A' : 'Angular', 'B' : 'Bash', 'C' : 'C++', 'D' : 'Docker'}
new_dict = dict1.copy()
print(new_dict)

empty_dict = new_dict.clear()
print(empty_dict)