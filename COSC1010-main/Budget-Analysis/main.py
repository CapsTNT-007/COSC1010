#
# Name Tayson Wheeler
# Date 9/22/24
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 
# Variables
budget = 0
expenses = 0
monthlyTotal = 0
moreExpenses = 'y'
extra = 0

# Getting information
budget = int(input("How much money do you have budgeted for this month?: $"))
moreExpenses = input("Do you have any expenses? (enter y for yes): ")

# Checking for y/n
while moreExpenses != 'y' and moreExpenses != 'n':
    moreExpenses = input("ERROR: Thats not in an acceptable format: Please type y or n: ")

# Monthly loop
while moreExpenses == 'y':
    expenses = int(input("How much did you spend?: $"))
    monthlyTotal += expenses
    moreExpenses = input("Do you have any more expenses?: (enter y for yes): ")
    while moreExpenses != 'y' and moreExpenses != 'n':
        moreExpenses = input("ERROR: Thats not in an acceptable format: Please type y or n: ")

# Checking if over or under
extra = budget - monthlyTotal
if extra > 0:
    print(f"You where ${extra} under budget.")
elif extra == 0:
    print(f"You where perfectly on budget.")
else:
    extra = extra - extra * 2
    print(f"You where ${extra} over budget.")