# print out a table of prime numbers

from prime import GetPrime

number = int(input("Enter amount of prime numbers: "))

counter = 1
primes = 0

# loop until raching the user-inputted number
while primes < number :

    # check if the number is prime
    if GetPrime(counter) :
        print(counter)
        primes = primes + 1
        
    counter = counter + 1
