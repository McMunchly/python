# play a full game of hangman

import random
import time
import os
clear = lambda: os.system('clear')

def Game():
    print("Loading new word...")
    word = GetWord()
    progress = ["_"] * len(word)
    guesses = 0
    invalid_guesses = 0
    max_guess = 6
    guesslist = []

    time.sleep(1)
    clear()
    
    while invalid_guesses < max_guess:
        dec_guess = True
        PrintWord(progress)
        PrintArt(invalid_guesses, max_guess)
        PrintGuesses(guesslist)
        
        #print("Guesses remaining: " + str(max_guess - invalid_guesses))
        guess = input("Guess your letter (type 'quit' to exit): ")
        guess = guess.upper()

        if(guess == "QUIT"):
            break;

        clear()
        if guess not in guesslist:
            guesslist.append(guess)
        else:
            print("You already guessed that letter")
            continue
        count = 0
        while count < len(word):
            if guess == word[count]:
                progress[count] = word[count]
                dec_guess = False
            count = count + 1

        if "_" not in progress:
            PrintWord(progress)
            print("-----------")
            print("You Win!!!")
            print("-----------")
            print("It took you " + str(guesses) + " tries to guess the word " + word)
            print()
            break;

        if dec_guess == True:
            invalid_guesses = invalid_guesses + 1

        guesses = guesses + 1

    if invalid_guesses == max_guess:
        PrintWord(progress)
        PrintArt(invalid_guesses, max_guess)
        print()
        print("Sorry, you lose")
        print("The word was " + str(word))
        print()


def GetWord():
    words = []

    with open("hangman.txt", "r") as file:
        word = file.readline().strip()
    
        words.append(word)
    
        while word:
            word = file.readline().strip()
            words.append(word)

    return words[random.randint(0, len(words))]

def PrintWord(theword):
    stretched = ""
    for letter in theword:
        stretched = stretched + letter + " "

    print(stretched)

def PrintArt(guesses, max_gs):
    print("______")
    print("     |")
    if(guesses >= 1):
        print("     0")
    if(guesses >= 2):
        print("     |")
    if(guesses >= 4):
        print("    /|\\")
    elif(guesses >= 3):
        print("    /|")
    if(guesses == 5):
        print("    /")
    elif(guesses == 6):
        print("    / \\")

    for x in range(0, max_gs - guesses):
        print()

def PrintGuesses(guesses):
    print("Current guesses:", end = " ")
    
    for letter in guesses:
        print(letter, end = " ")
        
    print()
        
if __name__ == "__main__":
    clear()
    print("-------------------------")
    print("---Welcome to Hangman!---")
    print("-------------------------")
    print("    by Samuel Dassler")
    print()
    play = "y"
        
    while play == "y":
        Game()
        play = input("Play? (y/n): ")
      
    
