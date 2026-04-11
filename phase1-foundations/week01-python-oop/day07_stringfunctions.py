"""
Day 05 — String functions
Phase 1, Week 1 | AI Learning Journey
Date: 11 April 2026

What I learned:
- recalling basics. (different string funcions : uppercase, lowercase, title case, replace, split, join)

"""

my_str = "Nishwa Prajapati, a grad STUDENT at Stevens Institute Of TECHnology!"
uppercase_str = my_str.upper() # does not work if my_str.upper() and print my_str
print("Uppercase string : ", uppercase_str)

lowercase_str = my_str.lower()
print("Lowercase string :", lowercase_str)

title_case = my_str.title()
print("Title string :", title_case)

new_str = my_str.replace("Prajapati", "Ashwin")
print("Replaced string : ", new_str)

split_str = my_str.split("a")
print("Split string : ", split_str)
split_str_1 = my_str.split("Stevens")
print(split_str_1)

join_str = "Nishwa Prajapati"
join_new_element = "-".join("Hello World")
print(join_new_element)
using_join = join_str.join("Hello")
print(using_join)
join_element = ".".join(join_str)
print("Joined :", join_element)


