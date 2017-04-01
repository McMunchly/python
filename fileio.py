sentence = input("Enter some text: ")

with open('textfile.txt', 'w') as file:
    file.write(sentence)
