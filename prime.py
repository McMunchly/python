# return whether a number is prime or not

def GetPrime(number):
    numRange = range(2, number)

    for element in numRange:
        if number % element == 0:
            return False

    return True
