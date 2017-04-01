# play rock, paper, scissors against the computer

import random

game = True;

# 0 = tie, 1 = win, 2 = loss
result = 0;

win = 0;
loss = 0;
tie = 0;

while(game == True):
    play = input("choose rock, paper, or scissors: ")

    if(play != "rock"):
        if(play != "paper"):
            if(play != "scissors"):
               print("not a valid play")
               continue
            
    # 1 = rock, 2 = paper, 3 = scissors
    ai = random.randint(1, 3)

    if(ai == 1):
        print("Computer plays rock")
    elif(ai == 2):
        print("Computer plays paper")
    else:
        print("Computer plays scissors")

    print("")
    
    if(play == "rock"):
        if(ai == 1):
            result = 0
        elif(ai == 2):
            result = 2
        else:
            result = 1
    elif(play == "paper"):
        if(ai == 1):
            result = 1
        elif(ai == 2):
            result = 0
        else:
            result = 2
    else:
        if(ai == 1):
            result = 2
        elif(ai == 2):
            result = 1
        else:
            result = 0
    
    if(result == 0):
        print("It's a tie.")
        tie = tie + 1
    elif(result == 1):
        print("You win!")
        win = win + 1
    else:
        print("You lose...")
        loss = loss + 1

    print("Your score is ", win, "-", loss, "-", tie,)

    print("")
    play = input("Play again? y/n: ")
    print("")
    
    if(play != "y"):
        game = False;

