# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:09:27 2022

@author: Sayali
"""

import os.path
from hamnosysdict import HamNoSysText as ham

text = input("Enter a word to convert to ISL - ")

#check is the sigml file exists
#exists() function returns True if the file exists
if(os.path.exists("C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\"+text+".sigml") == True):
    fp = open(r"C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\"+text+".sigml", 'r')
    #sendsigml(fp)
    fp.close()
    print("File present")
else:
    #create the sigml file
    #General info to make a sigml text work
    xml_version = '1.0'
    encoding = 'utf-8'
    preamble = '<?xml version="{}" encoding="{}"?>\n<sigml>\n\n'.format(xml_version, encoding)
    postamble = '</sigml>'
     
    flag = 0
    #print(len(ham))
    for i in ham.keys():
        #print(i)
        if(i == text):
            fp = open("C:\\Users\\Sayali\\Desktop\\project\\SigmlFiles\\"+text+".sigml", "w")
            # Writing content
            #Creates the contents of the SiGML file
            fp.write(preamble)
            fp.write('<hns_sign gloss = "'+text+'">\n')
            fp.write("<hamnosys_manual>\n")
            for j in ham[i]:
                fp.write("<"+j+"/>\n")
            fp.write("</hamnosys_manual>\n")
            fp.write("</hns_sign>\n")
            fp.write(postamble)
            fp.close()
            flag = 1
            break
    if flag == 0:
        print("Gloss not found")
    else:
        print("File created successfully")
        
    


                   
        
        
        
        
       
       
      