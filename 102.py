# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 13:14:02 2022

@author: Sayali
"""


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