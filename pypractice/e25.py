# have the computer guess your number
import statistics

number = int(input("Enter a number between 0 and 100: "))

guess = False
guesses = 1
num_list = [num for num in range(0, 101)]
print(num_list)
com_guess = int(statistics.median(num_list))
print(com_guess)
while guess == False or len(num_list) == 1:
    result = input("Is " + str(com_guess) + " your number? (y/n): ")
    
    if result == "y":
        guess = True
        break

    else:
        result = input("Too high or too low? (h/l): ")

    if result == "h":
        num_list = num_list[0:int(len(num_list) / 2)]
    else:
        num_list = num_list[int(len(num_list) / 2):]

    if len(num_list) > 1:
        com_guess = int(statistics.median(num_list))
    else:
        com_guess = num_list[0]
        print("Your number is " + str(com_guess))
        break

    guesses = guesses + 1
    
if com_guess != number:
    print("You inputted: " + str(number) + ". You are a liar")

else:
    print("Success! It took " + str(guesses) + " tries to guess your number")
