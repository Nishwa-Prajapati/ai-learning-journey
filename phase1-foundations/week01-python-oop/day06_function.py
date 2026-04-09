"""
Day 05 — Input function, Help function , Round function, Sum function, Absolute Function, Enumerate function, Zip function
Phase 1, Week 1 | AI Learning Journey
Date: 9 April 2026

What I learned:
- recalling basics (different types of function)

"""

# INPUT FUNCTION :   (User input is converterd to string)
# name = input("Enter your name :")
# print("Hello ",name)

# a = input("Enter no1 :")
# b = input("Enter no2 :")
# addition = a + b
# int_a = int(a)
# int_b = int(b)

# c = int_a + int_b

# print("Addition before converting to int :", addition)
# print("Addition after converstion is :", c)

# HELP FUNCTION : (executes the build in help system)
# help()

# ROUND FUNCTION : (rounds a number)
print(round(1.2))
print(round(1.6389))
print(round(3.6))
print(round(8.00))
print(round(7.1))

#round of till what number in decimal
print(round(3.456123,2))
print(round(6.577,1))
print(round(9.0000345672009,12))

# SUM FUNCTION : sum, min, max
# num_list = [2,45,78,"hello", 99, 00, "100"] -> ERROR as need all integer
num_list = [23.2 , 67 , 99 , 1 , 0.00 , 2]
print(max(num_list))
print(min(num_list))
print(sum(num_list))

# ABSOLUTE FUNCTION :  returns absolute value of a number
print(abs(-34))
print(abs(1))
print(abs(-78.90))
print(abs(0))

# ENUMERATE FUNCTION : Takes the collection and returns it as an enumerate object
example = [2,3,5,"hello"]
print(list(enumerate(example)))    #returns a list which has [(index,value itself)]

ex = {2,5,7}
print(set(enumerate(ex)))

x = (67,89,23.5)
print(tuple(enumerate(x)))

# ZIP FUNCTION : returns an iterator from two or more iterators
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
list3 = ["hello", 3]
print(list(zip(list1,list2)))
print(list(zip(list2,list3)))
print(list(zip(list3,list1)))


