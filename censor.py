# censors a certain word in a sentence

sentence = input("Enter a sentence: ")
blocked = input("Enter a word to censor: ")

def censor(text, word):
    words = text.split(" ")

    for e in range(0, len(words)):
        if words[e].lower() == word.lower():
            words[e] = '*' * len(word)
                
    return " ".join(words)

print(censor(sentence, blocked))
