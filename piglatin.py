# turn a phrase into pig latin

def PigLatin(word):
    # check for upper capitalized words
    upper = False
    if word[0].isupper():
        upper = True
    word = word.lower()

    # for voewl sounds, just as 'way' to the end without modifying the word
    if(word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u"):
        word = word + "w"

    # consonants up to the first vowel are move to back and 'ay' is added
    else:
        letter = 0

        while word[letter] != "a" and word[letter] != "e" and word[letter] != "i" and word[letter] != "o" and word[letter] != "u": 
            letter = letter + 1
        word = word[letter:] + word[0:letter]

    # recapitalize if needed
    if upper == True:
        word = word[0].upper() + word[1:]

    return word

def ToPigLatin(phrase):
    pyg = "ay"
    way = "way"

    newphrase = ""

    reverser = 0

    words = phrase.split(" ")
    print(words)
    
    while reverser < len(words) :
        newword = PigLatin(words[reverser]) + pyg

        # move periods to the back
        if("." in newword):
            newword = newword.replace(".", "")
            newword = newword + "."

        # add word to the phrase
        newphrase = newphrase + newword + " "
        reverser = reverser + 1

    return newphrase

def main():
    phrase = input()
    print(ToPigLatin(phrase))

if __name__ == "__main__":
    main()
    
