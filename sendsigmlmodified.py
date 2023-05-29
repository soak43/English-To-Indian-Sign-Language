# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:16:27 2022

@author: Sayali
"""


import socket
import time
'''
def remove_last_word(str,i):
    
    str.split() = wordlist
    wordlist = wordlist.pop(len(wordlist)-1)
    newstring = ""
    for word in wordlist:
        newstring = newstring + " " + word
    return newstring
'''

def send_sigml(sent):
    
    start = time.time()
    #sent = input("Enter an ISL sentence - ").lower()
    #print(sent)
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
    file_list = []
    for i in range(len(sentence)):
        print(len(sentence))
        print(sentence[i])
        file = "C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\" + sentence[i] +".sigml"
        file_list.append(file)
    
    print("File list = ", file_list)
    
    
    #Create a temp file
    
    temp_file = open("C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\temp.sigml", "w")
    xml_version = '1.0'
    encoding = 'utf-8'
    preamble = '<?xml version="{}" encoding="{}"?>\n<sigml>\n\n'.format(xml_version, encoding)
    postamble = '\n</sigml>'
    
    temp_file.write(preamble)
    
    for i in file_list:
        try:
            print("i = ", i)
            file = open(i)
            for line in file:
                temp_file.write(line)
        except(IOError):
            print("\nFile not found ", i)
    
    temp_file.write(postamble)
    
    #Close the file
    temp_file.close()
    
    #Opens the specified file, reads from it and sends the content to the SiGML Player via the socket
    f = open("C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\temp.sigml",'rb')
    l = f.read(BUFFER_SIZE)  
    #print(l)
    print("sending file:", f)
    while (l):
        s.sendall(l)
        print('Sent ', repr(l)) #if uncommented prints the contents of the file
        l = f.read(BUFFER_SIZE)
    f.close()
    
    
    #Lets the user know the files have successfully been sent
    print("file(s) sent")
    
    
    #Closes the connection
    s.close()
    print("connection closed")
    
    end = time.time()
    print("Time required to send sigml = ", end-start)