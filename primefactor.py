def IsPrime(num):
    if num > 1:

        for i in range(2,num):
            if (num % i) == 0:
                return False
            else:
                return True
     
    else:
         return False
 
num = int(input("Enter a number: "))

primes = []
check = num
smallest = 2

while True:
    
    if check == 1:
        break
    elif check % smallest == 0:
        primes.append(smallest)

        check = int(check / smallest)
    else:

        smallest = smallest + 1

        if IsPrime(smallest) and check % smallest == 0:
            primes.append(smallest)
            check = int(check / smallest)
    

print(primes)
