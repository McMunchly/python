# File fibonacci.py

limit = int(input("Enter number of fibonacci digits to display: "))

numbers = []

# the first two numbers of the sequence are 1
num1 = 1;
num2 = 1;

while(limit > 0):
    # add the first two digits first
    if(len(numbers) < 2):
        numbers.append(num1)

    # each number is teh sum of the previous two numbers
    else:
        num1 = numbers[len(numbers) - 1]
        num2 = numbers[len(numbers) - 2]
        numbers.append(num1 + num2)

    limit -= 1

# print each digit on it's own line for clarity
for element in numbers:
    print(element)
