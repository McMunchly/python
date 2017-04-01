# check if a user-inputted number is odd or even and check division

number = int(input("Enter an integer: "))

if(number % 4 == 0):
    print("Your number is divisible by 4!")
elif(number % 2 == 0):
    print("Your number is even")
else:
    print("Your number is odd")

num = int(input("Enter first number: "))
check = int(input("Enter second number: "))

numString = str(num)
checkString = str(check)

if(num % check == 0):
    print(str(check) + " goes into " + str(num) + " evenly " + str(num // check) + " times")
else:
    print(str(check) + " does not go into " + str(num) + " evenly ")
