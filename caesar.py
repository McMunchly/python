# encrypts a phrase with a Ceasar cipher

phrase = input("Enter a phrase: ")
number = int(input("Enter number of letters to shift: "))

coded = ""
lowerA = 97
upperA = 65
upper = 0;

for i in phrase:
    if str.isalpha(i):
        if str.isupper(i):
            upper = upperA
        else:
            upper = lowerA
            
        i = upper + ((ord(i) - upper) + number) % 26
        
        coded += chr(i)
    else:
        coded += i

print(coded);
    
