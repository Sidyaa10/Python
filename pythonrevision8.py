#Dictionary
#A dictionary is a sequence of key value or item pairs separated by commas
#In dictionary the key cannot be changed and the values can be repeated and changed
#A dictionary is an unordered collection and a dictionary is mutable

Dict={
      1:"Apollo",
      2:"Sid",
      3:"Buddha",
      4:"Hercules"
      }
print(Dict)
print(Dict[2])
Dict[2] = "SIDD"
print(Dict)
del Dict[2]
print(Dict)

#dictionary functions
print(len(Dict))
print(max(Dict))
print(min(Dict))

#dictionary methods
Dict1={
    1:'Butter Chicken',
    2:'Pasta',
    3:'Chinese',
    4:'Chicken Biryani'
}
print(Dict1)
Dict2=Dict1.copy()
print(Dict2)
print(Dict2.get(1,'Error Key Not Found'))
print(Dict2.get(5,'Error Key Not Found'))
print(Dict2.values())



