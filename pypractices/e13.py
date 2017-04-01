# create a fibonacci sequence up to a user-inputted length

limit = int(input("Enter number of fibonacci digits to display: "))

numbers = []

num1 = 1;
num2 = 1;

while(limit > 0):
    if(len(numbers) < 2):
        numbers.append(num1)
    else:
        num1 = numbers[len(numbers) - 1]
        num2 = numbers[len(numbers) - 2]
        numbers.append(num1 + num2)

    limit -= 1

print(numbers)
