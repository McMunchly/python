def gcd(a, b):
    if b == 0:
        return a
    else:
        print(a, b, a % b)
        return gcd(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(gcd(num1, num2))
