# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:09:02 2022

@author: Sayali
"""


import sys
import argparse
from nltk.parse.stanford import StanfordParser
from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tree import *
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
import os
import re
model = "C:\Stanford CoreNLPParser\stanford-corenlp-4.4.0\stanford-corenlp-4.4.0-models.jar"
jar = "C:\Stanford CoreNLPParser\stanford-corenlp-4.4.0\stanford-corenlp-4.4.0.jar"
java_path = "C:\Program Files\Java\jdk-16.0.2\bin\java.exe"
os.environ['CLASSPATH'] = "C:\Stanford CoreNLPParser\stanford-corenlp-4.4.0\stanford-corenlp-4.4.0.jar"
os.environ['JAVAHOME'] = java_path
pos_tagger = StanfordPOSTagger(model, jar, encoding=&#39;utf8&#39;)
inputString = &quot; &quot;

for each in range(1,len(sys.argv)):
inputString += sys.argv[each]
inputString += &quot; &quot;

inputString = input(&quot;Enter the String to convert to ISL: &quot;)
#inpstr=inputString.split(&#39;.&#39;)

inpstr=re.split(r&#39;[,]|[.]|[?].&#39;,inputString)
print (inpstr)
parser=StanfordParser(model_path=&#39;C:\\stanford-parser\\stanford-english-corenlp-2018-02-27-
models\\edu\\stanford\\nlp\\models\\lexparser\\englishPCFG.ser.gz&#39;)
c=0
# o=parser.parse(s.split())
for inputString in inpstr:
englishtree=[tree for tree in parser.parse(inputString.split())]
parsetree=englishtree[0]
dict={}

# &quot;***********subtrees**********&quot;

parenttree= ParentedTree.convert(parsetree)
for sub in parenttree.subtrees():
dict[sub.treeposition()]=0

#&quot;----------------------------------------------&quot;

isltree=Tree(&#39;ROOT&#39;,[])
i=0
for sub in parenttree.subtrees():
if(sub.label()==&quot;NP&quot; and dict[sub.treeposition()]==0 and dict[sub.parent().treeposition()]==0):
dict[sub.treeposition()]=1
isltree.insert(i,sub)
i=i+1

if(sub.label()==&quot;VP&quot; or sub.label()==&quot;PRP&quot;):

for sub2 in sub.subtrees():
if((sub2.label()==&quot;NP&quot; or sub2.label()==&#39;PRP&#39;)and dict[sub2.treeposition()]==0 and
dict[sub2.parent().treeposition()]==0):
dict[sub2.treeposition()]=1
isltree.insert(i,sub2)
i=i+1

for sub in parenttree.subtrees():
for sub2 in sub.subtrees():
# print sub2
# print len(sub2.leaves())
# print dict[sub2.treeposition()]
if(len(sub2.leaves())==1 and dict[sub2.treeposition()]==0 and
dict[sub2.parent().treeposition()]==0):
dict[sub2.treeposition()]=1
isltree.insert(i,sub2)
i=i+1

parsed_sent=isltree.leaves()

words=parsed_sent
#print(words)

stop_words=set(stopwords.words(&quot;english&quot;))
# print stop_words

lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

lemmatized_words=[]

for w in parsed_sent:
#w = ps.stem(w)
lemmatized_words.append(lemmatizer.lemmatize(w))

islsentence = &quot;&quot;
for w in lemmatized_words:
if (w.lower()) not in stop_words:
islsentence+=w
islsentence+=&quot; &quot;

print (islsentence)

from nltk.parse.stanford import StanfordDependencyParser
import numpy as np
import cv2
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.Clip import copy
import nltk
import os
import sys
#import pygame
from moviepy.editor import *

#from pygame import clip
try:
os.remove(&quot;my_concatenation.mp4&quot;)
except:
pass

print(sys.path)
name=&quot; &quot;

for each in range(1,len(sys.argv)):
name+=sys.argv[each]
name+=&quot; &quot;

input_text = islsentence

text = nltk.word_tokenize(input_text)

result=nltk.pos_tag(text)

for each in result:
print(each)

dict={}
dict[&quot;NN&quot;]=&quot;noun&quot;
arg_array=[]
try:
for text in result:

#arg_array.append(VideoFileClip(text[0]+&quot;_&quot;+dict[text[1]]+&quot;.mp4&quot;))
arg_array.append(VideoFileClip(&quot;F:\\Final ciil\\&quot;+text[0]+&quot;.mp4&quot;))
#print(text[0]+&quot;.mp4&quot;)
print(arg_array[0])
except:
print(&quot;Video doesn&#39;t exist in database or grammatical error&quot;)
sys.exit(0)

final_clip = concatenate_videoclips(arg_array)
final_clip.write_videofile(&quot;C:\\Users\\User\\Desktop\\my_concatenation&quot;+str(c)+&quot;.mp4&quot;)
os.startfile(&quot;C:\\Users\\User\\Desktop\\my_concatenation&quot;+str(c)+&quot;.mp4&quot;)
c=c+1