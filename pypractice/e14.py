# remove all duplicates numbers from a list - with a loop, and with a set

import random

a = []

limit = 10

listSize = 10

while listSize > 0 :
    a.append(random.randint(1, limit))
    listSize  = listSize - 1


def Loop(a):
    b = []
    for element in a :
        if element not in b :
            b.append(element)

    return b

def Set(a):
    return(set(a))
a.sort()
print("Original list:", a)
print("Using a loop:", Loop(a))
print("Using a set:", Set(a))
