# -*- coding: utf-8 -*-
"""
Created on Mon May  2 22:50:23 2022

@author: Sayali
"""


import os.path
from hamnosysdict import HamNoSysText as ham
from sendsigmlmodified import send_sigml
import time

def create_sigml(text):
    
    start = time.time()

    #text = input("Enter a sentence to convert to generate SIGML files - ").lower()
    '''
    for item in text:
        for i in item.split():
            list_text = i
    '''
    list_text = text.split()
            
    #Print the list of words
    print(list_text)
    print("Length = ",len(list_text))
    
    for m in range(len(list_text)):
        if(list_text[m].isnumeric() == True):
            print("Number - ", list_text[m])
            number_list = list(list_text[m])
            del list_text[m]
            print("Number is split as - ", number_list)
            print("List_text = ", list_text)
            if(len(list_text) != 1):
                for n in range(len(number_list)):
                    list_text.append(number_list[n])
                print("New list = ", list_text)
            #ltex = list_text
            
    for m in range(len(list_text)):
        flag = 0  #default consideration that the word is not present in the dictionary
        for n in ham.keys():
            if(list_text[m] == n):
                flag = 1   #word is present in the dictionary
                break
        if(flag == 0):
            word_list = list(list_text[m])
            print(list_text[m], " not present in the dictionary")
            del list_text[m]
            print("The word is split as - ", word_list)
            for k in range(len(word_list)):
                list_text.append(word_list[k])
            print("New list = ", list_text)
            
    
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
    listToStr = ' '.join([str(elem) for elem in list_text])
    print(listToStr)
    end = time.time()
    print("Time required to generate sigml files = ", end-start)
    
    send_sigml(listToStr)
         