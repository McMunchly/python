# rolls a set number of dice of a certain size and return the array of rolls
import random
random.seed

d4 = 4
d6 = 6
d8 = 8
d10 = 10
d12 = 12
d20 = 20

def RollDice(dice, sides):
        results = []
        total = 0

        for x in range(dice):
                die = random.randrange(1, sides + 1)
                total += die
                results.append(die)

        return results

def SumDice(dice):
        total = 0
        for x in range(len(dice)):
                total = total + dice[x]

        return total
