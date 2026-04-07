"""
Day 05 — List, Tuples, Dictionaries, Set
Phase 1, Week 1 | AI Learning Journey
Date: 6 April 2026

What I learned:
- Recalling the basics 

"""

# LIST contains any type of elements and is mutable (modifiable)
my_list = ["a", "b", "hello", "Good Morning", "Python", "AI-Learning"]
print(my_list)

flexible_list = [34 , 6789, "23", "apple", "google", "Nvidia"]
print(flexible_list)
print(type(flexible_list))

print(flexible_list[3])
print(flexible_list[0])

add_list = [2,3,67,8,10]
print("Addition of all elements of add_list is :", sum(add_list))
print("Length of the list : ", len(add_list))
add_list[2] = 1000
print(add_list)    #[2,3,1000,8,10]

mean_list = [12,24,34,54]
print("Mean of the given list  : ", sum(mean_list)/len(mean_list))

marks = [0,1,34,66,78,89]
mean_marks = sum(marks)/len(marks)
print("Average of marks  = ", mean_marks)

single_element_list = ['Hey', ]
print("Single Element -> ", single_element_list )

# TUPLE are immutable (can't be modified)
my_tuple = (1,2,"hello","68",34.8, "bye")
print(my_tuple)

single_element_tuple = (2,)
print("Single Element Tuple -> " , single_element_tuple)
print(type(single_element_tuple))

# my_tuple[0] = "Good"
# print(my_tuple) -> ERROR

#If want to change in tuple then convert to list then convert again to tuple to highligt change in tuple 
my_tuple_list = list(my_tuple)
my_tuple_list[0] = "good"
my_tuple = tuple(my_tuple_list)
print("Modified change in my_tuple using list conversion -> ", my_tuple)


# DICTIONARY {key:value} pair
my_dict = { 'Name' : 'Nishwa',
                'Place' : 'States',
                'Programming' : 'Python',
                'Semester' : ['Sem1', 'Sem2', 'Sem3', 'Sem4'],
                'Profesors' : {'DSA' : 'William Hendrix', 'DL' : 'Tian Han'} 
}

print(my_dict)
print(my_dict['Name'])
print(type(my_dict))
print(my_dict['Profesors'])

my_dict['Place'] = 'Gujarat'
print(my_dict['Place'])

my_dict['Hobby'] = 'Painting'
print(my_dict)
print(type(my_dict))

del my_dict['Semester']

print("\n -----------------------------")
print(my_dict)

print("\n ------------------------------")
print("All Keys :")
print(my_dict.keys())  #return keys of my_dict

print(list(my_dict.keys()))

print("\n ------------------------------")
print("All Values :")
print(my_dict.values())

print("\n ------------------------------")
print("All Items :")
print(my_dict.items())

print("\n ------------------------------")
print(my_dict['Profesors']['DSA']) # which Profesor teaches DSA 


# SET -  UNORDERED COLLECTION OF UNIQUE ELEMENTS & its mutable 
empty_set = set()
print(type(empty_set))

non_empty_set = {1, 45, "hello", 36.5}
print(non_empty_set)

non_empty_set = non_empty_set | {1,'Bye'}
print(non_empty_set)
print(len(non_empty_set))

my_object = {}
print(type(my_object)) #return dict sot if empty set you need to write set()


List = [1,1,1,4,5,45,4,5,6,9,9,2,3,1]
print(List)
print(type(List))

set_element = set(List)
print(set_element)
print(type(set_element))

# a set cannot have mutable items 
# my_set = {1,2,[3,4]}
# print(my_set)

# but we can have tuple here as it is immutable 
my_set = {1,2,(3,4)}
print(my_set)

# my_new_set = {3,4,{6,7}}
# print(my_new_set) # error here !!!












