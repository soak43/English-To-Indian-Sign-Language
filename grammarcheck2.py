# -*- coding: utf-8 -*-
"""
Created on Wed May 18 15:43:54 2022

@author: Sayali
"""
#import language_tool_python
#from stanandcore import convert_sentence
import time
from gingerit.gingerit import GingerIt

def grammarcheck():
    
    start = time.time()
     
    text = input("Enter a sentence >>: ")
    parser = GingerIt()
    
    corrected_text = parser.parse(text)
    print("correct sentence = ", corrected_text)
        
    end = time.time()
    print("Time required to run grammar check = ", end-start)

        
    
    
    #return correct_text.lower()

grammarcheck()