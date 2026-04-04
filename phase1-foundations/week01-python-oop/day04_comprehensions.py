"""
Day 04 — Comprehensions
Phase 1, Week 1 | AI Learning Journey
Date: 26 March 2026

What I learned:
- Lists of different comprehensions and how they are diffeent from eachother
- List comprehension, Set comprehension, Dictionary comprehension, Generator comprehension
- Its a short and clear way to form new sequences using existing iterables. 

"""


#List comprehensions

fruits = ['apple','mango','grapes']

#[expression for item in iterable if condition]
res = [fruits for fruit in fruits if fruits[1]== 'mango']
print(res)
res2 = [fruits for fruit in fruits if fruits[1]== 'kiwi']
print(res2)

#set comprehension
a = {6,12,6,24,24,24,24,35,41,6,52,64,6,77,6,89,90}
no = [num for num in a if num % 2 == 0]
print(no)

#dictionary comprehension 
#{key_expression : value_expression for item in iterable if condition}
states = ['Uttarpradesh','Gujarat','punjab','Maharashtra']
capitals = ['New delhi', 'Gandhinagar','Chandigarh','Mumbai']

res3 = {state : capital for state, capital in zip(states,capitals)}
print(res3)

#Generator comprehension 
res4 = (num for num in range(100) if num % 2 == 0)
print(list(res4))
# for num in res4:
#     print(num)