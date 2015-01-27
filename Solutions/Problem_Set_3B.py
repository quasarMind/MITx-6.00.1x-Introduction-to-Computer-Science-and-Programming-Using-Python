#Hangman Helper function No. One
for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
#Hangman Helper function No. Two
finalString = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            finalString += letter
        else:
            finalString += "_"+" "
    return finalString
#Hangman Helper function No. Three
alpha = "abcdefghijklmnopqrstuvwxyz"
#or import string
#alpha = string.ascii_lowercase
    stringFinal = ""
    for letter in alpha:
        if letter not in lettersGuessed:
            stringFinal += letter
    return stringFinal
