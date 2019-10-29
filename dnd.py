import random
import math
import dice

random.seed

abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
classes = [["Barbarian", dice.d12],["Bard", dice.d8],["Cleric", dice.d8],["Druid", dice.d8],
        ["Fighter", dice.d10],["Monk", dice.d8],["Paladin", dice.d10],["Ranger", dice.d10],
        ["Rogue", dice.d8],["Sorcerer", dice.d6],["Warlock", dice.d8],["Wizard", dice.d6]]
        
def GetAbilityModifier(score):
        return int(math.floor((score - 10) / 2))

def RollCharacter():
        amount = input("Enter character's name: ")

        # loop until the player enters a valid class number
        characterClass = -1
        while characterClass < 0 or characterClass > 11:
                for i in range(len(classes)):
                        print(str(i) + " - " + classes[i][0] + "\thit die: " + str(classes[i][1]))
                              
                characterClass = int(input(": "))

        stats = []
        total = 0
        j = 0
        x = 0;

        d6 = 6

        for x in range(len(abilities)):
                print(abilities[x] + " rolls: ")
                y = 0
                i = 0

                rolls = dice.RollDice(4, dice.d6)

                rolls.sort()
                rolls = rolls[len(rolls) - 3:]
                print(rolls)

                stats.append(dice.SumDice(rolls))

        print()
        print("your character's name is:", amount)
        print("your class is: ", classes[characterClass][0])

        print("HP: ", str(classes[characterClass][1] + GetAbilityModifier(stats[2])))
        
        for j in range(len(abilities)):
                print(abilities[j] + ":", stats[j])
                print("Your modifier is: " + str(GetAbilityModifier(stats[j])))

RollCharacter()
