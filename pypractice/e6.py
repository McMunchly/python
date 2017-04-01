# check if a string is a palindrome or not

string = input("Enter a string: ")

a = 0;
b = len(string);

match = True;

while a < b:
    if string[a] != string[b - 1 - a]:
        if(a != b):
            match = False;
            break;
    a += 1;

if(match == True):
    print("That word is a palindrome");
else:
    print("That word is not a palindrome");
