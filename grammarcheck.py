# -*- coding: utf-8 -*-
"""
Created on Thu May  5 21:12:14 2022

@author: Sayali
"""

import language_tool_python
from stanandcore import convert_sentence
import time

def grammar_check(text):
    
    start = time.time()
    
    tool = language_tool_python.LanguageTool('en-US')
    #text = input("Enter a sentence")
    #text = "Your the best but their are allso  good !"
    correct_text = tool.correct(text)
    
    end = time.time()
    print("Time required to run grammar check = ", end-start)
    
    if(correct_text.lower() == text.lower()):
        convert_sentence(correct_text.lower())
    else: 
        print("The corrected sentence is = ", correct_text)
        
    
    
    return correct_text.lower()
    
#grammar_check()