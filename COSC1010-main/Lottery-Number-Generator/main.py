#
# Name Tayson Wheeler
# Date 10/27/1014
# Lottery Number Generator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#import random modual
import random

#create list
lotteryNumber = [0] * 7

#assigning random values
for index in range (7):
    lotteryNumber[index] = random.randint(0,9)

#printing values
print("Here is you lottery numbers: ")
for index in range (7):
    print(lotteryNumber[index], end='')