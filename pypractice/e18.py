# play 'cows and bulls' with the computer

import random

# generate 4 digits that don't repeat
a = random.sample(range(0, 9), 4)

# make sure first digit isn't zero, because player can't input 0 as first digit
while a[0] == 0:
    a = random.sample(range(0, 9), 4)
    
game = True
guesses = 0
cows = 0
bulls = 0

repeats = []
    
while game == True :
    bulls = 0
    cows = 0
    del repeats[:]
    
    guesses = guesses + 1
    
    guess = int(input("Enter a 4-digit number (1000, 9999): "))

    if(guess < 1000 or guess > 9999):
        print("not a valid number")
        continue
    
    b = [int(element) for element in str(guess)]

    count = 0
    
    while count < 4:
        if(a[count] == b[count]):
            cows = cows + 1
            repeats.append(a[count])
            
        count = count + 1
        
    for element in b:
        if(element in a and element not in repeats):
            bulls = bulls + 1
            repeats.append(element)
            continue

    print(cows, bulls)

    if(cows == 4):
        game = False;

number = a[0] * 1000 + a[1] * 100 + a[2] * 10 + a[3]
print("It took you", guesses, "tries to guess the number", number) 
