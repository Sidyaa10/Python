#Collections
#Collection contains an items of same data type

#Counters
#counter is a container which tracks the frequency of value
from collections import Counter

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
count = Counter(fruits)
print(count)

#Deque
#deque is a double ended queue, it is like a hollow pipe open at both ends it allows addition and deletion of elements from both sides
from collections import deque

d = deque([1, 2, 3])
d.append(4)   # add to right
d.appendleft(0)  # add to left
print(d)  # Output: deque([0, 1, 2, 3, 4])

d.pop()  # remove from right
d.popleft()  # remove from left
print(d)  # Output: deque([1, 2, 3])

#Ordered Dictionary
#Ordered-Dictionary  is a subclass of the dictionary and it remembers the order in which the elements are added

from collections import OrderedDict

d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Accessing
print(d['a'])  # Output: 1


#Named Tuple
#Named tuple is gives you a special feature to create a new data type

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
p = Person('Sid', 23)
print(p.name)  # Output: John
print(p.age)   # Output: 30