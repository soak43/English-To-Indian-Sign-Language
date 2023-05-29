# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:43:35 2022

@author: Sayali
"""


import socket
#import sys
'''
def remove_last_word(str,i):
    
    str.split() = wordlist
    wordlist = wordlist.pop(len(wordlist)-1)
    newstring = ""
    for word in wordlist:
        newstring = newstring + " " + word
    return newstring
'''
sent = input("Enter an ISL sentence")
print(sent)
sentence = sent.split()
print(sentence)

#Initialises a socket object
#The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connects to the SiGML Player which listens on port 8052
#s.connect(("localhost", 8052))

#print("Connection established")

#Determines how many bites are sent per time step
BUFFER_SIZE = 4096

#s.sendall('alone')
file_list = []
for i in range(len(sentence)):
    print(len(sentence))
    print(sentence[i])
    file = "C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\" + sentence[i] +".sigml"
    file_list.append(file)

print("File list = ", file_list)

'''
#Establish connection
s.connect(("localhost", 8052))
print("Connection established")
'''

'''
if(len(sentence) > 1):
    for i in range(len(sentence)):
        f1 = "C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\" + sentence[i] +".sigml"
        string = open(f1,rb)
        newfile = remove_last_word(string,i)
        
'''    
for i in file_list:
    print("i = ", i)
    try:
        #Establish connection
        s.connect(("localhost", 8052))
        print("Connection established")
        #Opens the specified file, reads from it and sends the content to the SiGML Player via the socket
        f = open(i,'rb')
        l = f.read(BUFFER_SIZE)  
        #print(l)
        print("sending file:", i)
        while (l):
            s.sendall(l)
            print('Sent ', repr(l)) #if uncommented prints the contents of the file
            l = f.read(BUFFER_SIZE)
        f.close()
        
    except IOError:
        print("file: " + i + " not found")


#Lets the user know the files have successfully been sent
print("file(s) sent")


#Closes the connection
s.close()
print("connection closed")




    