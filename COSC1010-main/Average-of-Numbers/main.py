#
# Name Tayson Wheeler
# Date 10/20/24
# Average of Numbers Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#Opening file
number_file = open('numbers.txt','r')

#Initializing variables
total = 0
count = 0
average = 0

#Getting values
for line in number_file:
    #convert to float
    number = float(line)

    #add to count
    count += 1

    #add to total
    total += number

#Close file
number_file.close()

#Get and display average
average = total/count
print(f'The aveage is {average}.')