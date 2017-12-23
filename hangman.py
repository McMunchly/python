# play a full game of hangman

import random

def Game():
    print("Welcome to hangman!")
        
    word = GetWord()
    progress = ["_"] * len(word)
    guesses = 0
    invalid_guesses = 0
    max_guess = 6
    guesslist = []

    while invalid_guesses < max_guess:
        dec_guess = True
        PrintWord(progress)
        PrintArt(invalid_guesses, max_guess)
        #print("Guesses remaining: " + str(max_guess - invalid_guesses))
        guess = input("Guess your letter: ")

        guess = guess.upper()

        if(guess == "QUIT"):
            print("Quitting...")
            break;
        
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

        if("_" not in progress):
            PrintWord(progress)
            print("You Win!")
            print("It took you " + str(guesses) + " tries to guess the word " + word)
            break;

        if(dec_guess == True):
            invalid_guesses = invalid_guesses + 1

        guesses = guesses + 1

    if(invalid_guesses == max_guess):
        PrintArt(invalid_guesses, max_guess)
        print("Sorry, you lose")
        print("The word was " + str(word))


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
    if(guesses >= 1):
        print("     O")
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
        print("")
             
if __name__ == "__main__":
    Game()
    
