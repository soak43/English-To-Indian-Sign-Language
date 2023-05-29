# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:31:13 2022

@author: Sayali
"""


import nltk
nltk.download('stopwords')
import time
from nltk.tree import *
from nltk import tokenize
from nltk.parse import ViterbiParser
from nltk import PCFG
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import stop_words
from stop_words import get_stop_words



'''
examp_pcfg = PCFG.fromstring("""
S -> NP VP [1.0]
NP ->  NP PP [0.4]|'school'[0.1] | 'today'[0.18] | 'saw'[0.04] | 'stars'[0.18] |'tonight'[0.1]
VP -> VP PP [0.3] | V NP [0.7] 
V -> 'saw' [0.5] | 'went' [0.5]
PP -> P NP [0.5] | 'i' [0.5]
P -> 'with' [0.5] |'in' [0.5]
""")
'''

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


englishtree=[tree for tree in parses]
parsetree=englishtree[0]
dict={}

parenttree= ParentedTree.convert(parsetree)
for sub in parenttree.subtrees():
    dict[sub.treeposition()]=0


isltree=Tree('ROOT',[])
i=0
for sub in parenttree.subtrees():
    if(sub.label()=="NP" and dict[sub.treeposition()]==0 and dict[sub.parent().treeposition()]==0):
        dict[sub.treeposition()]=1
        isltree.insert(i,sub)
        i=i+1
        
    if(sub.label()=="VP" or sub.label()=="PRP"):
        for sub2 in sub.subtrees():
            if((sub2.label()=="NP" or sub2.label()=='PRP')and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
                dict[sub2.treeposition()]=1
                isltree.insert(i,sub2)
                i=i+1
for sub in parenttree.subtrees():
    for sub2 in sub.subtrees():

        if(len(sub2.leaves())==1 and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
            dict[sub2.treeposition()]=1
            isltree.insert(i,sub2)
            i=i+1
 
parsed_sent=isltree.leaves()
words=parsed_sent

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
lemmatized_words=[]

for w in parsed_sent:
    w = ps.stem(w)
    lemmatized_words.append(lemmatizer.lemmatize(w))

islsentence = ""
print(lemmatized_words)

#Stop word removal
stop_words = stopwords.words('english')
#print(stop_words)

without_stop_words = []
for word in lemmatized_words:
    if word not in stop_words:
        without_stop_words.append(word)
print(without_stop_words)

for w in without_stop_words:
    islsentence+=w
    islsentence+=" "
        

print(islsentence)



#num_parses = len(parses)
#print('Time(secs #Parses')
#print('------------------------------')
#print('%11.4f%11d'%(time,num_parses))

#from nltk.draw.tree import draw_trees
#draw_trees(*parses)

#for parse in parses:
  # print(parse)