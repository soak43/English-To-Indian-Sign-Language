# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:24:41 2022

@author: Sayali
"""


#from nltk.parse.stanford import StanfordDependencyParser
#import numpy as np
#import cv2
import imageio
#imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip, concatenate_videoclips
#from moviepy.editor import VideoFileClip, concatenate_videoclips
#from moviepy.Clip import copy
import nltk
import os
import sys
#import pygame
from moviepy.editor import *
c = 0

#from pygame import clip
try:
	os.remove("my_concatenation.mp4")
except:
    pass

print(sys.path)
name=" "

for each in range(1,len(sys.argv)):
    name+=sys.argv[each]
    name+=""

input_text = input("Enter a sentence in ISL")

text = nltk.word_tokenize(input_text)

result=nltk.pos_tag(text)

for each in result:
    print(each)

dict={}
dict["NN"]="noun"
arg_array=[]
try:
	for text in result:
		#arg_array.append(VideoFileClip(text[0]+&quot;_&quot;+dict[text[1]]+&quot;.mp4&quot;))
		arg_array.append(VideoFileClip("C:\\Final ciil\\"+text[0]+".mp4"))
		#print(text[0]+&quot;.mp4&quot;)
		print(arg_array[0])
except:
	print("Video doesn't exist in database or grammatical error")
sys.exit(0)

final_clip = concatenate_videoclips(arg_array)
final_clip.write_videofile("C:\\Users\\User\\Desktop\\my_concatenation"+str(c)+".mp4")
os.startfile("C:\\Users\\User\\Desktop\\my_concatenation"+str(c)+".mp4")
c=c+1
