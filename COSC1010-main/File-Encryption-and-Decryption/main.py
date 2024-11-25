#
# Name Tayson Wheeler
# Date 11/24/2024
# File Encryption and Decryption Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

#opening files
data = open('text.txt','r')
outFile = open('encrypted.txt','w')

#establishing dictionary
encryptionData = {'A':'あ','a':'い','B':'う','b':'え',
                  'C':'お','c':'か','D':'き','d':'く',
                  'E':'け','e':'こ','F':'さ','f':'し',
                  'G':'す','g':'せ','H':'そ','h':'た',
                  'I':'ち','i':'つ','J':'て','j':'と',
                  'K':'な','k':'に','L':'ぬ','l':'ね',
                  'M':'の','m':'は','N':'ひ','n':'ふ',
                  'O':'へ','o':'ほ','P':'ま','p':'み',
                  'Q':'む','q':'め','R':'も','r':'や',
                  'S':'ゆ','s':'よ','T':'ら','t':'り',
                  'U':'る','u':'れ','V':'ろ','v':'わ',
                  'W':'ゐ','w':'ゑ','X':'を','x':'ん',
                  'Y':'っ','y':'ゝ','Z':'ぱ','z':'ぴ',
                ' ':'-','1':'1','2':'2','3':'3','4':'4',
                '5':'5','6':'6','7':'7','8':'8','9':'9',
                '0':'0',',':',','.':'.','-':'_',"'":'^'}

#establishing variables
fullLine = ''
characterToAdd = ''

#main code starts
for line in data:
    for character in line:
        for key in encryptionData:
            #looks to see if the character is in the dictionary
            if character == key:
                #converts character to encrypted character
                characterToAdd = str(encryptionData[key])
                #adds encrypted character to eachother to create a line
                fullLine = "".join([fullLine, characterToAdd])
    #writes encrypted line to file
    with open('encrypted.txt','a', encoding='utf8') as outFile:
        outFile.write(fullLine +'\n')
        #closes file
        outFile.close()
    #resets line variable
    fullLine = ''
#close file
data.close()

#2nd program
#opens file
with open('encrypted.txt','r', encoding='utf8') as encrypted:
        #prints file
        for line in encrypted:
            for character in line:
                for key in encryptionData:
                    #looks to see if the character is in the dictionary
                    if character == encryptionData[key]:
                        #converts character to decrypted character
                        characterToAdd = str(key)
                        #adds decrypted character to eachother to create a line
                        fullLine = "".join([fullLine, characterToAdd])
            #prints line and resets variable
            print(fullLine)
            fullLine = ''
#closes file
encrypted.close()