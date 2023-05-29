# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 20:29:22 2022

@author: Sayali
"""


import socket
#import sys

sent = input("Enter an ISL sentence - ")
print(sent)
sentence = sent.split()
print(sentence)


#Initialises a socket object
#The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol. 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connects to the SiGML Player which listens on port 8052
s.connect(("localhost", 8052))

print("Connection established")

#Determines how many bites are sent per time step
BUFFER_SIZE = 4096

#s.sendall('alone')

for i in range(len(sentence)):
    file = "C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\" + sentence[i] +".sigml"
    try:
        #Opens the specified file, reads from it and sends the content to the SiGML Player via the socket
        f = open(file,'rb')
        l = f.read(BUFFER_SIZE)  
        #print(l)
        print("sending file:", file)
        while (l):
            s.sendall(l)
			#print('Sent ', repr(l)) #if uncommented prints the contents of the file
            l = f.read(BUFFER_SIZE)
        f.close()
    except IOError:
        print("file: " + file + " not found")

#Lets the user know the files have successfully been sent
print("file(s) sent")

#Closes the connection
s.close()
print("connection closed")




    