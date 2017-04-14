# encrypts or decrypts a phrase with a Ceasar cipher

lowerA = 97
upperA = 65

def CaesarEncrypt(toencrypt, key):

    coded = ""
    upper = 0;
    
    for i in toencrypt:
        if str.isalpha(i):
            if str.isupper(i):
                upper = upperA
            else:
                upper = lowerA
                
            i = upper + ((ord(i) - upper) + key) % 26
            
            coded += chr(i)
        else:
            coded += i

    return coded

def CaesarDecrypt(todecrypt, key):
    
    coded = ""
    upper = 0;
    
    for i in todecrypt:
        if str.isalpha(i):
            if str.isupper(i):
                upper = upperA
            else:
                upper = lowerA
                
            i = upper + ((ord(i) - upper) - key) % 26
            
            coded += chr(i)
        else:
            coded += i

    return coded

if __name__ == "__main__":
    phrase = input("Enter a phrase: ")
    number = int(input("Enter number of letters to shift: "))

    print("\nEncrypted:")
    phrase = CaesarEncrypt(phrase, number)
    print(phrase)
    print("\nDecrypted:")
    print(CaesarDecrypt(phrase, number))
    
