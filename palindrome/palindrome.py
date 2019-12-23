import string

def pal(word):
    if len(word) <= 1:
       return True
    elif word[0] != word[len(word) - 1]:
        return False
    elif word[0] == word[len(word) - 1]:
        return pal(word[1:-1])

def prepword(word, lower, space):

    if not lower:
        word = word.lower()
    if not space:
        word = word.replace(" ", "")

    return word


