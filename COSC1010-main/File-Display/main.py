#
# Name Tayson Wheeler
# Date 10/20/24
# File Display Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#Open file
files_numbers = open('numbers.txt','r')

#Read file and print
for line in files_numbers:
    number = int(line)
    print(number)

#Close file
files_numbers.close()