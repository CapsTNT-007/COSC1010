#
# Name Tayson Wheeler
# Date 11/17/24
# Capital Quiz Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

import random

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South       Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    # Local variables
    stateQuestion = 0
    cont = 'y'
    countC = 0
    countI = 0
    guess = 0

    # Continue until user quits the game.
    while cont == 'y':

        #Gets a random question
        stateQuestion = random.choice(list(capitals))
        guess = input("What is the capital of {}? ".format(stateQuestion))

        #Sees if they input the right or wrong answer
        if guess == capitals[stateQuestion]:
            print('Horray! You are correct!')
            countC += 1
            cont = input('Do you want to continue?(y to continue, else to end) ')
        else:
            print('Uh oh, you got that inccorect.')
            countI += 1
            cont = input('Do you want to continue?(y to continue, else to end) ')

    #Prints results
    print('Congradualtions, you got', countC, 'correct, and', countI, 'incorrect.')

# Call the main function.
main()
