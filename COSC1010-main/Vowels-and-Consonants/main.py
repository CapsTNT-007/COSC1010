#
# Name Tayson Wheeler
# Date 11/10/24
# Vowels and Consonants Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#Defining funtions
def numberVowels(word):
    #Defining vowels and variables
    vowles = ['a','e','i','o','u']
    vowelCount = 0

    #Checking each charecter for if its a vowel
    for charecter in word:
        if charecter.lower() in vowles:
            vowelCount += 1
    
    #Returing numeric amount
    return(vowelCount)

def numberConstants(word):
    #Defining vowels and variables
    vowels = ['a','e','i','o','u']
    charecterCount = 0

    #Checking each charecter for if its a vowel
    for charecter in word:
        if charecter.lower() not in vowels:
            charecterCount += 1

    #Returing numeric amount
    return(charecterCount)

#Getting word and printing information
myWord = input("Enter a string of charecters")
print("The sting has", numberVowels(myWord), "vowels, and", numberConstants(myWord), "constants.")