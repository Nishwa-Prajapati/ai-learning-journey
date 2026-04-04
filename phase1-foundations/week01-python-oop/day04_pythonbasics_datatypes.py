#Datatypes 

#basic arithmetic
x=40
y=70
a=2
b=3
z=x*y
print("z")
print(z)

print(a+b)
print(type(x-b))

p=40%2
print(p)

q=2**3
print(q)
type(q)


#String
my_first_string = "Hello,Today the weather is good!!"
my_first_string

print(my_first_string)
type(my_first_string)

phrase = "Hello muddy, It was nice meeting you the other day."
print(phrase)
phrase.replace('muddy','buddy')
print(phrase)

new_phrase = phrase.replace('muddy','buddy')
print(new_phrase)

#Basic operations 
subject = 'Neural Networks'
print(len(subject))

print(subject)

subject.count('Ne')
print(subject.count('Ne'))

print(subject.count(' '))
counts = subject.count('s')
# print("The occurance od 's' in subject :" + counts)  -> concate can be done in str + str not str + int 
print("The occurence od 's' in subject :" + str(counts))

book = "I have recently found my interest towards reading books where I chose Agentic Artificial Intelligence as my first preference. It aligns with my interest so there's no second thought about spending my money in it."
i_count = book.count('i')
print("Total occurence of 'i' is :" + str(i_count))

only_i_count = book.lower().count('i')
print("Occurence of lower i (includes all i/I): " + str(only_i_count))



