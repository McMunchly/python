import random
import dice

random.seed

amount = input("Enter character's name: ")

labels = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
stats = []
total = 0
j = 0
x = 0;

d6 = 6

for x in range(len(labels)):
	print(labels[x] + " rolls: ")
	y = 0
	i = 0

	rolls = dice.RollDice(4, dice.d6)

	rolls.sort()
	rolls = rolls[len(rolls) - 3:]
	print(rolls)

	stats.append(dice.SumDice(rolls))


print("your character's name is:", amount)

for j in range(len(labels)):
	print(labels[j] + ":", stats[j])
