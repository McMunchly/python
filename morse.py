# translates a phrase into morse code

morse = {
    # punctuation
    " " : "/",
    "." : ".-.-.-",
    "," : "--..--",
    "-" : "-....-",
    "'" : ".----.",
    "?" : "..--..",
    ":" : "---...",
    "/" : "-..-.",
    "\n" : "\n",
    
    # letters
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",

    # numbers
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    }

def ToMorse(phrase):
    phrase = phrase.upper()
    
    translated = ""

    for key in phrase:
        translated = translated + morse[key] + " "

    return translated

def FromMorse(phrase):
    phrase = phrase.split(" ")
    
    tuples = morse.items()
    translated = ""

    for key in phrase:
        for item in tuples:
            if(key == item[1]):
                translated = translated + item[0]

    return translated

def main():
    sentence = input("Enter a phrase: ")
    morsecode = ToMorse(sentence)
    print(morsecode)
    print(FromMorse(morsecode))

if __name__ == "__main__":
    main()
