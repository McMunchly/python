# pick a random word from a dictionary

import random

def GetWord():
    words = []

    with open("sowpods.txt", "r") as file:
        word = file.readline().strip()
    
        words.append(word)
    
        while word:
            word = file.readline().strip()
            words.append(word)

    return words[random.randint(0, len(words))]

if __name__ == "__main__":
    print(GetWord())
