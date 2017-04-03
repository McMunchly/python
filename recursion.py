def factorial(n):
    #print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        #print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

def summation(n):
    if n == 1:
        return 1
    else:
        num = n + summation(n - 1)
        return num

print("Recursive factorial: " + str(factorial(5)))
print("rescursive summation: " + str(summation(5)))
