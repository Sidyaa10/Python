#list methods

list=['Apollo', 'Sid', 'Hercules', 'Buddha', 'Sun Wu Kong']
list.append('Beelzebub')
print(list)
list1=['Thor','Tesla']
list.extend(list1)
print(list)
print(list.count('Sid'))
print(list.remove('Sid'))

list1=[12,3,4,5,64,865,2]
list1.sort()
print(list1)
list1.pop()
print(list1)
#list comprehension
list2= [2,3,4,5,6]
list3=[]
for each in list2:
    list3.append(each*each)
print(list3)