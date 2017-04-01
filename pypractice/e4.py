# get all divisors of a user-inputted number

number = int(input("Input a number: "))

numRange = range(1, number + 1)

for element in numRange:
    if number % element == 0:
        print(element)
