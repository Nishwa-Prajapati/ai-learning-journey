"""
Day 05 — Indexing & slicing
Phase 1, Week 1 | AI Learning Journey
Date: 7 April 2026

What I learned:
- Recalling the basics 

"""

# INDEXING : 0   1   2   3   4     Positive indexing
#           -5  -4  -3  -2  -1     Negative indexing 
my_string = "Hello Tuesday..!!!"
print(my_string[0])
print(my_string[-1])
print(my_string[-6])

my_tuple = (1,2,45,78,33,12)
print(my_tuple[2])

my_list = ['Hello', 'Bye', 12, 67, 98.2]
print(my_list[1])
# print(my_list[7])  //out of range 

# my_set = {34,56,7,2}      set does not support indexing
# print(my_set[1])

my_dict = {'name' : 'Nishwa' , 'Surname' : 'Prajapati', 'State' : 'Gujarat'}
print(my_dict['name'])
# print(my_dict[0])   //always use key 

members = ['Raj','Om','Preet', 'Pranjal', 'Khushi', 'Diya', 'Kunal', 'Tirth', 'Mitwa', 'Rahul', 'Prem']
team1 = [members[0],members[2],members[4],members[6],members[8],members[10]]
team2 = [members[1],members[3],members[5],members[7],members[9]]
print("Team 1 contains members -> ", team1)
print("Team 2 contains members -> ", team2)

# SLICING  : extracting a portion of a sequence  (index like indexing 0 to ... and -1 to...)
#    sequence[start, stop, skip]   -> start include, stop exclude

my_fruits = "apple Orange Banana Kiwi Guava Watermelon Muskmelon !!!"
print(my_fruits[2:6])
print(my_fruits[0:])
print(my_fruits[:])
print(my_fruits[:10])
print(my_fruits[1:10:2])
print(my_fruits[::2])
print(my_fruits[3::3])

print(my_fruits[-1:])
print(my_fruits[::-1])
print(my_fruits[::-2])
print(my_fruits[-4::-2])

slice_tuple = (1,2,3,4)
print(slice_tuple[1:])
print(slice_tuple[:2])

slice_list = ["hello", 38.89, "bye", 2, 3 , 4, "Good morning", 45, 88888, "tata"]
print(slice_list[2:4])
print(slice_list[3:])
print(slice_list[1:9:2])

# Dictionary dont support slicing as it is unordered










