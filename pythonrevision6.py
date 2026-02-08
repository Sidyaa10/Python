#Lists
#lists are mutable

List=[1,2,3,4,5,6]
print(List)

#list operations
list=[1,2,3,4,5,6]
print(list[0])
print(list[1:3])#slicing list

List1=['Hulk','Thor','Hawkeye','Captain']
print(List1)
List1[3] ='Captain-America'
print(List1)

Civil_War=['Hulk', 'Thor', 'Hawkeye', 'Captain-America','Ant-Man']
del Civil_War[0:2]
print(Civil_War)

#list functions
list2=[12,1,2,3,4,5,6]
print(len(list2))
print(max(list2))
print(min(list2))
print(sorted(list2))