# RUN THIS FILE IN TERMINAL!!

import palindrome
import os.path

def testword(word, case, space):

    word = palindrome.prepword(word, case, space)

    print("is |" + word + "| a palindrome?: " + str(palindrome.pal(word)))

case = False
space = False

while True:
    lower = str(input("case-sensitive? (y/n): "))
    lower = lower.lower()
    if lower == "y":
        case = True
        break
    elif lower == "n":
        
        break

while True:
    lower = str(input("whitespace sensitive? (y/n): "))
    lower = lower.lower()
    if lower == "y":
        space = True
        break
    elif lower == "n":
        break
            
# see if a save file exists
with open("test.txt", "r") as file:
    while True:
        word = file.readline().strip()

        if word:
            testword(word, case, space)
        if not word:
            break
        
