import random
random.seed

print("LORELEI sent out DEWGONG!")
print("Go! PRIMATE!")
print("PRIMATE used RAGE!")

count = int(input("How many tries to escape?: "))

for x in range(0, count):
    pp = 20
    while pp > 0:
        rando = random.randint(0, 256)
            
        if rando == 256:
            print("PRIMATE's attack missed!")
            pp -= 1
        else:
            break
    
    if(pp == 0):
        print("PRIMAPE used STRUGGLE!");
    else:
        print("Attempt " + str(x + 1) + ": failed at pp = " + str(pp))

print("Enemy DEWGONG used REST!")
