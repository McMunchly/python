# print the largest number of a given list

import random

def Largest(nums):
    print(nums)
    
    largest = 0

    for num in nums:
        if num > largest:
            largest = num

    return largest


numlist = [random.randrange(0, 100, 1) for _ in range(random.randrange(3,10,1))]
print(Largest(numlist))
