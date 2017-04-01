# make a list containing the first and last elements of a different list

import random

def FirstLast(a):
    b = [a[0], a[len(a) - 1]]

    return b

limit = 25
rangeLimit = 50

a = random.sample(range(1, rangeLimit), random.randint(1, limit))

print(a)
print(FirstLast(a))
