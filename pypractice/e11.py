# check if a number is prime or not

def CheckPrime(number):
    
    numRange = range(2, number)

    for element in numRange:
        if number % element == 0:
            return False

    return True

number = int(input("Input a number: "))

if CheckPrime(number) == True :
    print("Your number is a prime number!")
else :
    print("Your number is not a prime number...")
