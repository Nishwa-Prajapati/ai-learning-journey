"""
Day 05 — Sort list and other more methods
Phase 1, Week 1 | AI Learning Journey
Date: 11 April 2026

What I learned:
- recalling basics. (sorting list, append, update, replace)

"""

# SORTING LIST
list1 = [1,2,56,78,22,1,0,53,90,92,12,23,43,77,3,0,2,6,8,11]
sorted_list = sorted(list1)
print("Sorted list :", sorted_list)

set1 = {2,3,45,1,0,45,55,23}
sorted_set = sorted(set1)
print("Sorted set :", sorted_set)

# tuple1 = ("hello", 34, 1, 0 ,"bye")      - > doesnot support sorting between int and str
# sorted_tuple = sorted(tuple1)
# print("Sorted tuple :", sorted_tuple)



# APPEND ELEMENT
list2 = [23,"hello", 1]
list2.append("Morning")
# my_list = list2.append("Morning") -> not working 
print("New list : ", list2)
# list2.append("bye",67)
# print("New appended list :", list2) -> only taked 1 argument

# UPDATE 
dict1 = {"Name" : "Nishwa", "Age" : 22, "Hobby" : "coding"}
# dict1.update({"age" : 34, "Name" : "Nishwa Prajapati"})    #append age : 34 as its Age not age 
dict1.update({"Age" : 34, "Name" : "Nishwa Prajapati"})
print( "Update dict :", dict1)

list_element = [12,34,"hello"]
list_element[1] = "Apple"
print("Update list :", list_element)


# REPLACE
my_str = "Hello world!!!"
new_str = my_str.replace("world", "python")
print("New string :", new_str)

# list3 = ["hello", 23, 11]        -> list has no attribute replace
# new_list = list3.replace(23,46)
# print("new list :", new_list)








