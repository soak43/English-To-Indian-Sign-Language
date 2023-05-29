# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 11:49:55 2022

@author: Sayali
"""


import os.path
from hamnosysdict import HamNoSysText as ham

text = input("Enter a sentence to convert to generate SIGML files - ").lower()
'''
for item in text:
    for i in item.split():
        list_text = i
'''
list_text = text.split()
        
#Print the list of words
print(list_text)
print("Length = ",len(list_text))

for j in range(len(list_text)):
    #check is the sigml file exists
    #exists() function returns True if the file exists
    if(os.path.exists("C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\"+list_text[j]+".sigml") == True):
        fp = open(r"C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\"+list_text[j]+".sigml", 'r')
        fp.close()
        print("File present - ", list_text[j])
    else:
        flag = 0
        #print(len(ham))
        for i in ham.keys():
            #print(i)
            if(i == list_text[j]):
                fp = open("C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\"+list_text[j]+".sigml", "w")
                # Writing content
                #Creates the contents of the SiGML file
                fp.write('<hns_sign gloss = "'+list_text[j]+'">\n')
                fp.write("<hamnosys_manual>\n")
                for k in ham[i]:
                    fp.write("<"+k+"/>\n")
                fp.write("</hamnosys_manual>\n")
                fp.write("</hns_sign>\n")
                fp.close()
                flag = 1
                break
        if flag == 0:
            print("Gloss not found")
        else:
            print("File created successfully - ", list_text[j])
     