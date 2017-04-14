# encrypts a phrase with a Ceasar cipher

phrase = input("Enter a phrase: ")
number = int(input("Enter number of letters to shift: "))

coded = ""
lowerZ = 122
upperZ = 90
upper = 0;

for i in phrase:
    if str.isalpha(i):
        if str.isupper(i):
            upper = upperZ
        else:
            upper = lowerZ
            
        i = ord(i) + number
        
        if(i > upper):
            i = i - 26

        coded += chr(i)
    else:
        coded += i

print(coded);
    
