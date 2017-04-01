# get all comment elements in two lists with list comprehension

import random

limit = 25
rangeLimit = 50

a = random.sample(range(1, rangeLimit), random.randint(1, limit))
b = random.sample(range(1, rangeLimit), random.randint(1, limit))

c = [element for element in a if element in b]

print(a)
print(b)
print(c)
