# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:28:25 2022

@author: Sayali
"""


import nltk
import time
from nltk.tree import *
from nltk import tokenize
from nltk.parse import ViterbiParser
from nltk import PCFG
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer


examp_pcfg = PCFG.fromstring("""
S -> NP VP [1.0]
NP ->  NP PP [0.4]|'astronomers'[0.1] | 'ears'[0.18] | 'saw'[0.04] | 'stars'[0.18] |'telescopes'[0.1]
VP -> VP PP [0.3] | V NP [0.7] 
V -> 'saw' [1.0] 
PP -> P NP [1.0]
P -> 'with' [1.0] 
""")

sent = 'astronomers saw stars with telescopes'
tokens = sent.split() 

#tokenizing the sentence

parser = ViterbiParser(examp_pcfg)
print('\n sent: %s\nparsser: %s\n grammar: %s' %(sent,parser,examp_pcfg))
parser.trace(0)
t = time.time()

parses = parser.parse_all(tokens)
time = time.time() - t
num_parses = len(parses)
print('Time(secs #Parses')
print('------------------------------')
print('%11.4f%11d'%(time,num_parses))

from nltk.draw.tree import draw_trees
draw_trees(*parses)

for parse in parses:
   print(parse)