# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:26:12 2022

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
import socket

#from createclip import create_video
#----------------------------#

def try_port(port=0):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))

    p = sock.getsockname()[1]
    sock.close()

    return p
    
def convert_sentence(input_string: str):
    java_path = 'C:\Program Files\Java\jdk-16.0.2\bin\java.exe'
    os.environ['CLASSPATH'] = java_path


    if input_string.split() == 1:
        return None
    
    '''
    if len(input_string.split()) == 1:
        path = create_video(input_string)
        return path
    '''
    
    port = None
    corenlp_options = None
    if corenlp_options is None:
           corenlp_options = ["-preload", "tokenize,ssplit,pos,lemma,parse,depparse"]
    if port is None:
        try:
            port = try_port(9000)
        except OSError:
            port = try_port()
            corenlp_options.append(str(port))
    else:
        try_port(port)


    parser = CoreNLPParser(url='http://localhost:{port}')

    englishtree = [tree for tree in parser.parse(input_string.split())]
    parsetree = englishtree[0]


    dict = {}

    # parenttree = ParentedTree(node=parsetree, children=[])
    parenttree = ParentedTree.fromstring(str(parsetree))

    # print("Input Sentence: ", input_string)
    # print("Input Sentence Tree\n")
    # print(parenttree)
    print("\n\n")

    for sub in parenttree.subtrees():
        dict[sub.treeposition()] = 0

    #----------------------------#

    islTree = Tree('ROOT', [])
    i = 0

    for sub in parenttree.subtrees():
        if (sub.label() =="NP" and dict[sub.treeposition()] == 0 and dict[sub.parent().treeposition()] == 0):
            dict[sub.treeposition()] = 1
            islTree.insert(i, sub)
            i = i + 1

        if(sub.label()=="VP" or sub.label()=="PRP"):
            for sub2 in sub.subtrees():
                if((sub2.label()=="NP" or sub2.label()=='PRP') and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
                    dict[sub2.treeposition()] = 1
                    islTree.insert(i,sub2)
                    i=i+1


    for sub in parenttree.subtrees():
        for sub2 in sub.subtrees():
            if(len(sub2.leaves())==1 and dict[sub2.treeposition()]==0 and dict[sub2.parent().treeposition()]==0):
                dict[sub2.treeposition()]=1
                islTree.insert(i,sub2)
                i=i+1

    parsed_sent = islTree.leaves()

    # words = parsed_sent

    # print("ISL Tree\n")
    # print(islTree)
    # print("\n\n")

    # nltk.download('stopwords')
    # nltk.download('wordnet')
    # print()

    stop_words = set(stopwords.words("english"))

    lemmantizer = WordNetLemmatizer()
    # ps = PorterStemmer()
    lemmantized_words = []


    for w in parsed_sent:
        # w = ps.stem(w)
        lemmantized_words.append(lemmantizer.lemmatize(w))

    islSentence = ""

    for w in lemmantized_words:
        if w not in stop_words:
            islSentence += w
            islSentence += " "

        # islSentence += w
        # islSentence += " "

    print("ISL Sentence\n")
    print(islSentence)
    # print("\n\n")
    #path = create_video(islSentence)

    #return path

def main():
    sent = input("Enter a sentence = ")
    convert_sentence(sent)

if __name__ == "__main__":
    main()