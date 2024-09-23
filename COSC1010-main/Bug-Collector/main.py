#
# Name Tayson Wheeler
# Date 9/22/24file
# Bug Collector Programming Project
# COSC 2409 DNT
#
# Initialize variables for bugs and total number of bugs collected.
bugs = 0
bugsInDay = 0
# Get number of bugs collected each day using a for loop.
for num in range (5):
    bugsInDay = int(input("How many bugs did you get today? "))
    bugs += bugsInDay
# Display the total number of bugs collected.
if bugs == 1:
    print("You collected" , bugs, "bug")
else:
    print("You collected" , bugs, "bugs")