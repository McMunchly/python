# turn a phrase into pig latin

def ReplacePeriod(word):
    newword = word
    
    if("." in word):
        newword = word.replace(".", "")
        newword = newword + "."

    return newword

def PigLatin(word):
    # check for upper capitalized words
    upper = False
    if word[0].isupper():
        upper = True
    word = word.lower()
    word = word + "-"
    
    # for vowel sounds, just as 'way' to the end without modifying the word
    if(word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u"):
        word = word + "w"

    # consonants up to the first vowel are move to back and 'ay' is added
    else:
        letter = 0
        while word[letter] != "a" and word[letter] != "e" and word[letter] != "i" and word[letter] != "o" and word[letter] != "u" and word[letter] != "y":
            letter = letter + 1

            if letter == len(word) - 1:
                letter = 1
                break;
            
        word = word[letter:] + word[0:letter]

    # recapitalize if needed
    if upper == True:
        word = word[0].upper() + word[1:]

    return word

def ToPigLatin(phrase):

    newphrase = ""

    reverser = 0

    words = phrase.split(" ")
    
    while reverser < len(words) :
        newword = PigLatin(words[reverser]) + "ay"

        # move periods to the back
        newword = ReplacePeriod(newword)

        # add word to the phrase
        newphrase = newphrase + newword + " "
        reverser = reverser + 1

    return newphrase

def FromPigLatin(phrase):

    newphrase = ""

    words = phrase.split(" ")

    for word in words:

        # check for upper capitalized words
        upper = False
        period = False
        if word[0].isupper():
            upper = True
        word = word.lower()

        if("." in word):
            word = word[:len(word) - 1]
            period = True
    
        if(word[len(word) - 3:] == "way"):
            word = word[:len(word) - 4]
        else:
            word = word[0:len(word) - 2]
            split = word.split("-")
            word = split[1] + split[0]

        if(upper == True):
            word = word.capitalize()

        if(period == True):
            word = word + "."
            
        newphrase = newphrase + word + " "
            
    return newphrase
    
def main():
    choice = input("Translate to or from from Pig Latin? (t/f): ")
    phrase = input("Enter a phrase: ")
            
    if(choice == "t"):
        print(ToPigLatin(phrase))
    else:
        print(FromPigLatin(phrase))

if __name__ == "__main__":
    main()
    
