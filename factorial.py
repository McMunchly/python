# prints a factorial

number = int(input("Enter which factorial you want: "))

def factorial(x):
    total = 1
    
    for number in range(1, x + 1):
        total = total * number
        
    return total

print(factorial(number))
