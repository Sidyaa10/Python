#lists Functions

lucky_numbers=[2,4,6,8,10]
Gods=["Vishnu","Sun Wu Kong","Shiva","Apollo","Thor"]

#to merge two lists together
Gods.extend(lucky_numbers)
print(Gods)

#to add a element to the list
Gods.append("Buddha")
print(Gods)

#helps add a element in a specific index and pushes the element resting there forward
Gods.insert(1,"Buddha")
print(Gods)

#remove a element from the lists
Gods.remove("Buddha")
print(Gods)

#pop a element from the lists
Gods.pop()
print(Gods)

#to determine the index of an element
print(Gods.index("Thor"))

#to see duplicate elements in a lists
print(Gods.count("Thor"))

#sorts a list in alphabetical order
Gods0=["Vishnu","Sun Wu Kong","Shiva","Apollo","Thor"]
Gods0.sort()
print(Gods0)

#reverse a list
Gods0.reverse()
print(Gods0)

#copy a list
Gods1= Gods0.copy()
print(Gods1)