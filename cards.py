import random

deck = []

def CreateDeck():
    for i in range(0,4):
        deck.append([])
        deck[i] = [j for j in range(2, 15)]

def DealCards():
    for i in range(0, 7):
        randsuit = random.randint(0, len(deck) - 1)
        randval = random.randint(0, len(deck[randsuit]) - 1)

        if randsuit == 0:
            print("\u2660", str(deck[randsuit][randval]))
        elif randsuit == 1:
             print("\u2665", str(deck[randsuit][randval]))
        elif randsuit == 2:
            print("\u2666", str(deck[randsuit][randval]))
        elif randsuit == 3:
             print("\u2663", str(deck[randsuit][randval]))
             
        del deck[randsuit][randval]

def PrintDeck():
        for i in range(0,4):
            if i == 0:
                print("\u2660", deck[i])
            elif i == 1:
                 print("\u2665", deck[i])
            elif i == 2:
                print("\u2666", deck[i])
            elif i == 3:
                 print("\u2663", deck[i])

CreateDeck()
DealCards()
PrintDeck()
