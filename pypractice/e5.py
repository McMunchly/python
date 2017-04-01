# take two random lists and find all common elements

import random

limit = 25
rangeLimit = 50

a = random.sample(range(1, rangeLimit), random.randint(1, limit))
b = random.sample(range(1, rangeLimit), random.randint(1, limit))

newList = []

if(len(a) > len(b)):
    for element in a:
        if(element in b):
            newList.append(element)
else:
    for element in b:
        if(element in a):
            newList.append(element)

print(a)
print(b)

newList.sort()

print(newList)
