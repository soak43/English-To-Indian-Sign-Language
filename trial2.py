# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:51:35 2022

@author: Sayali
"""


import sys
import os
import argparse

from nltk.parse.corenlp import CoreNLPParser
from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tree import Tree, ParentedTree
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import nltk

#from createclip import create_video
#----------------------------#
stop_words = set(stopwords.words("english"))
print(stop_words)
