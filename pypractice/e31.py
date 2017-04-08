# guess missing letters until a word is found

from e30 import GetWord

def PrintWord(theword):
    stretched = ""
    for letter in theword:
        stretched = stretched + letter + " "

    print(stretched)
    
word = GetWord()
progress = ["_"] * len(word)
guesses = 0
guesslist = []

print("Welcome to hangman!")
while "_" in progress:
    PrintWord(progress)
    guess = input("Guess your letter: ")

    guess = guess.upper()
    
    if guess not in guesslist:
        guesslist.append(guess)
    else:
        print("You already guessed that letter")
        continue
    count = 0
    while count < len(word):
        if guess == word[count]:
            progress[count] = word[count]
        count = count + 1

    guesses = guesses + 1

PrintWord(progress)
print("It took you " + str(guesses) + " to guess the word " + word)


