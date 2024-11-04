#
# Name Tayson Wheeler
# Date 11/3/24
# Magic 8 Ball Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#variables
anotherQuestion = 'y'

#inport random
import random

#open, read, and close file
infile = open('8_ball_responses.txt','r')
anwsers = infile.readlines()
infile.close

#strip \n
for index in range(len(anwsers)):
    anwsers[index] = anwsers[index].rstrip('\n')

while anotherQuestion == 'y':
    #ask question
    input('Ask a yes or now question and recive and answer. ')

    #select random
    selected = random.sample(anwsers, k=1)

    #print
    print('Your answer is:')
    print(selected)

    anotherQuestion = input("Do you have another question? (enter y for yes) ")
    while anotherQuestion != 'y' and anotherQuestion != 'n':
        anotherQuestion = input('ERROR: Thats not in an acceptable format: Please type y or n: ')