# reverse the words in a sentence

sentence = input("Enter a sentence: ")

newsentence = ""

words = sentence.split(" ")

reverser = len(words) - 1

while reverser >= 0 :
    newsentence = newsentence + words[reverser] + " "
    reverser = reverser - 1

print(newsentence)
