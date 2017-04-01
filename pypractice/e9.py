#guess a number the computer is thinking of

import random

number = random.randint(1, 9)
guess = 0;

guesses = 0;

while(guess != number):
    guess = int(input("Guess a number from 1-9: "))
    guesses += 1
    
    if(guess < 1):
        print("not a valid input")
        continue
    if(guess > 9):
        print("not a valid input")
        continue
    
    if(guess < number):
        print("too low")
    elif(guess > number):
        print("too high")
    else:
        print("You win!")

print("It took you", guesses, "tries to guess correctly.")
print("")
