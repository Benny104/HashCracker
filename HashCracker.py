#Author: Benny
import hashlib

#Opens the "PassList" file and strips nonprintable characters
list = open("PassList.txt")
passList = [line.strip() for line in list]

#Takes the user inputted hash
userHash = str(input("Please input your hash: "))

#Hashes each word from the "PassList"
for i in passList:
    encodedWord = i.encode()
    hashedWord = hashlib.sha256(encodedWord)
    hashedHex = hashedWord.hexdigest()

    #Compares user input with "i" from passList
    if userHash == hashedHex:
        print("Your word was:", i)





