# use binary search to find an element in a list

import random
import time

start_time = time.time()

a = random.sample(range(0, 1000), 500)
a.sort()
print(a)

number = int(input("Which number do you want to search for: "))

def BinarySearch(a, number):
    while len(a) != 1:
        half = int(len(a) / 2)
        
        if(number < a[half]):
           a = a[0:half]
        else:
            a = a[half:]

    return a[0]

def ForSearch(a, number):
    for element in a:
        if(number == element):
            return element;

if(number == BinarySearch(a, number)) :
    print("The number was found with binary search")
else:
    print("The number was not found with binary search")

if(number == ForSearch(a, number)) :
    print("The number was also found with a for loop")
else:
    print("The number was also not found with a for loop")
