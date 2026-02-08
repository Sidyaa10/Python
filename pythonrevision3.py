#String
#A string is a sequence which consists of 0 or more characters
#String is an immutable datatype

str=("hello, world")
print(str)
print(id(str)) #to learn the id of str

str=("hello, world")
print(len(str))

movie="Sleepless in Seatle"
print(len(movie))
print(movie[13])#to print the character at a specific index, it starts at 0

#Slicing for substrings
movie="Two weeks notice"

print(movie[0:3])
print(movie[:6])
print(movie[:9])
