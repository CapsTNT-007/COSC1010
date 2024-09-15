#
# Name Tayson Wheeler
# Date 9/14/24
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Local variables
areaA = 0
areaB = 0
# Get length A
lengthA = int(input('What is the length of triangle A? '))
# Get width A
widthA = int(input('What is the width of triangle A? '))
# Get length B
lengthB = int(input('What is the length of triangle B? '))
# Get width B
widthB = int(input('What is the width of triangle B? '))
# Calculate area A
areaA = (lengthA)*(widthA)
# Calculate area B
areaB = (lengthB)*(widthB)
# Print area comparison using if-elif-else statements
if (areaA)>(areaB):
    print('Triangle A has a bigger area')
elif (areaA)<(areaB):
    print('Triangle B has a bigger area')
else:
    print('The triangles have the same area')
