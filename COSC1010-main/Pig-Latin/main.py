#
# Name Tayson Wheeler
# Date 11/10/24
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#Get sentance and define variables
userSentance = input("What sentance would you like to convert to Pig Latin? ")
index = 0

#Split sentance into words
wordList = userSentance.split()

#Define a function that converts each word
def makePigLatin(currentWord):
    newWordStart = currentWord[1:]
    newWordEnd = currentWord[0]
    finalWord = newWordStart + newWordEnd + "ay"
    return(finalWord)

#Uses the 'makePigLatin' function on each word to convert it
for word in wordList:
    wordList[index] = makePigLatin(wordList[index])
    index += 1

#joins the end words into a string and prints
pigLatin = ' '.join(wordList)
print(pigLatin)