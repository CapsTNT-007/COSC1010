#
# Name Tayson wheeler
# Date 10/27/2024
# Exception Handling Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#Initializing variables

total = 0
count = 0
average = 0

#Opening file + try
try:
    number_file = open('numbers.txt','r')

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

#exceptions
except IOError:
    print('An error occoured trying to read the file.')

except ValueError:
    print('Non-numeric data found in the file.')
