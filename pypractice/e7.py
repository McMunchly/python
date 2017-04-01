# get a random list then filter only even numbers

import random

limit = 25
rangeLimit = 50

a = random.sample(range(1, rangeLimit), random.randint(1, limit))
a.sort()

b = [element for element in a if element % 2 == 0]

print(a)
print("Only evens:")
print(b)
