#
# Name Tayson Wheeler
# Date 9/29/24
# Feet to Inches Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program.

def feet_to_inches(feet):
    return feet * 12

# Main code
feet = int(input("How many feet would you like to convert to inches? "))
print(feet, "feet equals", feet_to_inches(feet),"inches.")