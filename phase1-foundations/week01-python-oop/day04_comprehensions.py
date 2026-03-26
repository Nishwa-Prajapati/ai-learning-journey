#List comprehensions

fruits = ['apple','mango','grapes']

#e[xpression for item in iterable if condition]
res = [fruits for fruit in fruits if fruits[1]== 'mango']
print(res)
res2 = [fruits for fruit in fruits if fruits[1]== 'kiwi']
print(res2)

#set comprehension
a = {6,12,6,24,24,24,24,35,41,6,52,64,6,77,6,89,90}
no = [num for num in a if num % 2 == 0]
print(no)

#dictionary comprehension 
states = ['Uttarpradesh','Gujarat','punjab','Maharashtra']
capitals = ['New delhi', 'Gandhinagar','Chandigarh','Mumbai']

res3 = {state : capital for state, capital in zip(states,capitals)}
print(res3)

#Generator comprehsion 
res4 = (num for num in range(100) if num % 2 == 0)
print(list(res4))
# for num in res4:
#     print(num)