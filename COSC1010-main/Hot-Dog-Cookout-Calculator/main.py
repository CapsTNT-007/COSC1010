#
# Name Tayson Wheeler
# Date 9/14/24
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Variables
hotdogsInPacks = 10
bunsInPacks = 8
requestedAmount = 0
requiredHotdogPacks = 0
requiredBunPacks = 0

#getting information
people = int(input('How many people will be at the cookout? '))
hotdogsPerPerson = int(input('How many hot dogs does each person want? '))

#Solving for packs of hotdogs needed
requestedAmount = (people)*(hotdogsPerPerson)
requiredHotdogPacks = (requestedAmount//hotdogsInPacks)
requiredBunPacks = (requestedAmount//bunsInPacks)
if (requiredHotdogPacks)*(hotdogsInPacks) == (requestedAmount):
    print ('Packs of hotdog needed:')
    print (requiredHotdogPacks)
else:
    requiredHotdogPacks = requiredHotdogPacks + 1
    print ('Packs of hotdog needed:')
    print (requiredHotdogPacks)

#Solving for packs of buns needed
if (requiredBunPacks)*(bunsInPacks) == (requestedAmount):
    print ('Packs of buns needed:')
    print (requiredBunPacks)
else:
    requiredBunPacks = requiredBunPacks + 1
    print ('Packs of buns needed:')
    print (requiredBunPacks)

#Finding extras
print ('Extra hotdogs:')
print ((requiredHotdogPacks)*(hotdogsInPacks)-(requestedAmount))
print ('Extra hotdogs:')
print ((requiredBunPacks)*(bunsInPacks)-(requestedAmount))