# turn a phrase into pig latin

pyg = "ay"
way = "way"

sentence = input("Enter a sentence: ")

newsentence = ""

words = sentence.split(" ")

reverser = 0

def PigLatin(word):
    # look for consonant clusters
    upper = False
    if word[0].isupper():
        upper = True
    word = word.lower()
    
    if(word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u"):
        word = word + "w"
    else:
        letter = 0

        while word[letter] != "a" and word[letter] != "e" and word[letter] != "i" and word[letter] != "o" and word[letter] != "u": 
            letter = letter + 1
        word = word[letter:] + word[0:letter]

    if upper == True:
        word = word[0].upper() + word[1:]

    return word

while reverser < len(words) :
    newword = PigLatin(words[reverser]) + pyg

    if("." in newword):
        newword = newword.replace(".", "")
        newword = newword + "."
    newsentence = newsentence + newword + " "
    reverser = reverser + 1

print(newsentence)
