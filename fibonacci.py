# File fibonacci.py

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

for element in numbers:
    print(element)
