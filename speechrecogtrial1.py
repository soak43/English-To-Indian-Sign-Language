# -*- coding: utf-8 -*-
"""
Created on Mon May  2 22:45:07 2022

@author: Sayali
"""

import speech_recognition as sr
#from stanandcore import convert_sentence
from grammarcheck import grammar_check
import time

def getaudio():
    start = time.time()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")   
    end = time.time()
    print("Time required to run speech recognition = ", end-start)
    grammar_check(text)
    return text
    
            
            
#getaudio()