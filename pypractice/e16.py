# generate either a strong or a weak password

import random

number = int(input("Input how long do you want your password to be: "))

password = ""

underscoreGap = random.randint(3, 6)

while number > 0 :
    if(underscoreGap == 0 and number != 1):
        password = password + "_"
        underscoreGap = random.randint(3, 6)
        
    else:
        num = random.randint(48, 122)
        
        if (num >= 91 and num <= 96) or (num >= 58 and num <= 64):
            num = num + random.randint(10, 20)
            
        password = password + str(chr(num))

    number = number - 1
    underscoreGap = underscoreGap - 1

print("Your password is:", password)
