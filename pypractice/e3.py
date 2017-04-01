# print out all numbers in the list that are less than a user-inputted number

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

limit = int(input("Enter a number: "))


for element in a:
    if element < limit:
       b.append(element)

print(b)
